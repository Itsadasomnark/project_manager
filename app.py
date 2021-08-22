import maya.cmds as mc
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from shiboken2 import wrapInstance
from shiboken2 import getCppPointer
import maya.OpenMayaUI as mui
import os, time
import json
import shutil
import shotgun_api3
import ui
reload(ui)
import c_dialog as cui
reload(cui)
import captureui as capui
reload(capui)
global path
global sg
sg = shotgun_api3.Shotgun("https://itsada.shotgrid.autodesk.com", "testAPI", "egpNjhz*0yxleliarmpnmdszc")

class Mainapp(QtWidgets.QMainWindow):
	"""docstring for app"""
	def __init__(self, parent=None):
		super(Mainapp, self).__init__(parent=parent)
		self.ui = ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.file_path = ''
		global path
		script_path = os.path.realpath(__file__)
		file_name = str(script_path).split('\\')[-1:]
		self.path_module = str(script_path).split('\\%s'%file_name[0])[0]
		self.path_module = self.path_module.replace('\\','/')
		with open('{}/root/root.json'.format(self.path_module)) as json_file:
			path = json.load(json_file)
		self.ui.textEdit.setText(path)
		self.setup_defaults()
		self.connect()
		self.capture = Capture(getMayaWindow())
	def setup_defaults(self):
		self.setWindowTitle('Project Manager')
		self.ui.project_combo.clear()
		self.ui.Listitem.clear()
		self.ui.department_combo.clear()
		self.ui.Task_combo.clear()
		self.ui.Listitem.clear()
		self.ui.Listfile.clear()
		self.ui.workspace.setChecked(True)
		self.update_project()
		self.AssetorShot()
		self.update_deparment()
		self.update_task()
		self.update_item()
		self.ui.version_combo.clear()
	
	def connect(self):
		self.ui.project_combo.currentIndexChanged.connect(self.AssetorShot)
		self.ui.AssetorShot.currentIndexChanged.connect(self.update_deparment)
		self.ui.AssetorShot.currentIndexChanged.connect(self.update_item)
		self.ui.department_combo.currentIndexChanged.connect(self.update_task)
		self.ui.newproject.clicked.connect(self.create_project)
		self.ui.path_Button.clicked.connect(self.get_path)
		self.ui.workspace.toggled.connect(self.update_version)
		self.ui.Task_combo.currentIndexChanged.connect(self.update_item)
		self.ui.Listitem.itemSelectionChanged.connect(self.update_version)
		self.ui.version_combo.currentIndexChanged.connect(self.update_file)
		self.ui.save.clicked.connect(self.save)
		self.ui.open_button.clicked.connect(self.open_file)
		self.ui.import_button.clicked.connect(self.import_file)
		self.ui.ref_button.clicked.connect(self.ref_file)
		self.ui.newdepartment.clicked.connect(self.create_department)
		self.ui.Newtask.clicked.connect(self.create_task)
		self.ui.newAssetorShot.clicked.connect(self.create_item)
		self.ui.Listfile.itemSelectionChanged.connect(self.setinfo)
		self.ui.publish_button.clicked.connect(self.publish)
	
	def setinfo(self):
		file = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		stat = os.stat(file)
		self.ui.textinfo.clear()
		self.ui.textinfo.append('Create Time : {}'.format(time.ctime(stat.st_ctime)))
		self.ui.textinfo.append('Last Modified : {}'.format(time.ctime(stat.st_mtime)))
		file_path = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		self.ui.label.setPixmap(QtGui.QPixmap(file_path))	
		#self.ui.label.setScaledContents(True)

	def get_path(self):
		fileDir = QtWidgets.QFileDialog.getExistingDirectory()
		with open('{}/root/root.json'.format(self.path_module), 'w') as jsonfile:
			json.dump(fileDir, jsonfile, sort_keys=True, indent=4)
		global path
		path = fileDir
		self.ui.textEdit.setText(fileDir)
		self.setup_defaults()
	
	def update_project(self):
		self.ui.project_combo.clear()
		if path != '':
			allproject = os.listdir(path)
			self.ui.project_combo.addItems(allproject)
			for project in range(len(allproject)):
				fullpath = '{}/{}'.format(path,allproject[project])
				self.ui.project_combo.setItemData(project, fullpath, QtCore.Qt.UserRole)
			self.ui.project_combo.currentIndexChanged.emit(True)
	
	def AssetorShot(self):
		project = self.ui.project_combo.itemData(self.ui.project_combo.currentIndex(), QtCore.Qt.UserRole)
		if project != None:
			self.ui.AssetorShot.blockSignals(True)
			item = os.listdir(project)
			Afullpath = '{}/asset'.format(project)
			Bfullpath = '{}/shot'.format(project)
			self.ui.AssetorShot.setItemData(0, Afullpath, QtCore.Qt.UserRole)
			self.ui.AssetorShot.setItemData(1, Bfullpath, QtCore.Qt.UserRole)
			self.ui.AssetorShot.blockSignals(False)
			self.ui.AssetorShot.currentIndexChanged.emit(True)
		else:
			self.ui.AssetorShot.setItemData(0, None, QtCore.Qt.UserRole)
			self.ui.AssetorShot.setItemData(1, None, QtCore.Qt.UserRole)
	
	def update_deparment(self):
		AssetorShot = self.ui.AssetorShot.itemData(self.ui.AssetorShot.currentIndex(), QtCore.Qt.UserRole)
		if AssetorShot != None:
			alldepartment = os.listdir(AssetorShot)
			self.ui.department_combo.blockSignals(True)
			self.ui.department_combo.clear()
			self.ui.department_combo.addItems(alldepartment)
			for department in range(len(alldepartment)):
				fullpath = '{}/{}'.format(AssetorShot,alldepartment[department])
				self.ui.department_combo.setItemData(department, fullpath, QtCore.Qt.UserRole)
			self.ui.department_combo.blockSignals(False)
			self.ui.department_combo.currentIndexChanged.emit(True)
		else:
			self.ui.department_combo.clear()
	
	def update_task(self):
		deparment = self.ui.department_combo.itemData(self.ui.department_combo.currentIndex(), QtCore.Qt.UserRole)
		if deparment != None:
			alltask = os.listdir(deparment)
			self.ui.Task_combo.blockSignals(True)
			self.ui.Task_combo.clear()
			self.ui.Task_combo.addItems(alltask)
			for task in range(len(alltask)):
				fullpath = '{}/{}'.format(deparment,alltask[task])
				self.ui.Task_combo.setItemData(task, fullpath, QtCore.Qt.UserRole)
			self.ui.Task_combo.blockSignals(False)
		else:
			self.ui.Task_combo.clear()
		self.ui.workspace.toggled.emit(True)
	def update_item(self):
		task = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole)
		if task != None:
			allitem = os.listdir(task)
			self.ui.Listitem.blockSignals(True)
			self.ui.Listitem.clear()
			for name in allitem:
				item = QtWidgets.QListWidgetItem()
				item.setText(name)
				fullpath = '{}/{}'.format(task,name)
				item.setData(QtCore.Qt.UserRole, fullpath) 
				self.ui.Listitem.addItem(item)
			self.ui.Listitem.blockSignals(False)
			self.ui.Listfile.clear()
		else:
			self.ui.Listitem.clear()
			self.ui.Listfile.clear()
			self.ui.version_combo.clear()
	
	def update_version(self):
		listitem = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole) + '/' + self.ui.Listitem.currentItem().text()
		if self.ui.workspace.isChecked() == True: 
			self.ui.version_combo.clear()
			self.ui.Listfile.clear()
			self.ui.save.setEnabled(True)
			self.ui.publish_button.setEnabled(True)
			listitem = listitem + '/workspace'
			for (root, dirs, files) in os.walk(listitem, topdown=True):
				for file in files:
					item = QtWidgets.QListWidgetItem()
					item.setText(file)
					fullpath = '{}/{}'.format(root,file)
					item.setData(QtCore.Qt.UserRole, fullpath)
					self.ui.Listfile.addItem(item)
		else:
			listitem = listitem + '/publish'
			self.ui.save.setEnabled(False)
			self.ui.publish_button.setEnabled(False)
			allversion = os.listdir(listitem)
			self.ui.version_combo.blockSignals(True)
			self.ui.version_combo.clear()
			self.ui.version_combo.addItems(allversion)
			for version in range(len(allversion)):
				fullpath = '{}/{}'.format(listitem,allversion[version])
				self.ui.version_combo.setItemData(version, fullpath, QtCore.Qt.UserRole)
			self.ui.version_combo.blockSignals(False)
			self.ui.version_combo.currentIndexChanged.emit(True)
		self.ui.textinfo.clear()

	def update_file(self):
		version = self.ui.version_combo.itemData(self.ui.version_combo.currentIndex(), QtCore.Qt.UserRole)
		if version != None:
			allfile = os.listdir(version)
			self.ui.Listfile.clear()
			for file in allfile:
				item = QtWidgets.QListWidgetItem()
				item.setText(file)
				fullpath = '{}/{}'.format(version,file)
				item.setData(QtCore.Qt.UserRole, fullpath)
				self.ui.Listfile.addItem(item)
		else:
			self.ui.Listfile.clear()

	def create_project(self):
		global create
		dirname = path
		create = filename_ui(dirname, 'project', getMayaWindow())
		try:
			create.close()
		except:
			pass
		create.exec_()

	def create_department(self):
		global create
		dirname = self.ui.project_combo.itemData(self.ui.project_combo.currentIndex(), QtCore.Qt.UserRole)
		dirname += '/{}'.format(self.ui.AssetorShot.currentText())
		create = filename_ui(dirname, 'department', getMayaWindow())
		try:
			create.close()
		except:
			pass
		create.exec_()

	def create_task(self):
		global create
		dirname = self.ui.department_combo.itemData(self.ui.department_combo.currentIndex(), QtCore.Qt.UserRole)
		create = filename_ui(dirname, 'task', getMayaWindow())
		try:
			create.close()
		except:
			pass
		create.exec_()

	def create_item(self):
		global create
		dirname = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole)
		create = filename_ui(dirname, 'item', getMayaWindow())
		try:
			create.close()
		except:
			pass
		create.exec_()
	
	def open_file(self):
		file = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		mc.file(new=True, force=True) 
		mc.file(file, o=True)

	def ref_file(self):
		file = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		mc.file(file, r=True)

	def import_file(self):
		file = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		mc.file(file, i=True)

	def save(self):
		project = self.ui.project_combo.currentText()
		department = self.ui.department_combo.currentText()
		task = self.ui.Task_combo.currentText()
		item_name = self.ui.Listitem.currentItem().text()
		file_name = '{}_{}_{}_{}'.format(project, department, task, item_name)
		savepath = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole) + '/' + self.ui.Listitem.currentItem().text()
		if self.ui.workspace.isChecked() == True: 
			savepath = savepath + '/workspace'
		file = os.listdir(savepath)
		count = len(file)+1
		os.mkdir('{}/V{:03d}'.format(savepath,count))
		savepath += '/V{:03d}'.format(count)
		file_name += '_V{:03d}'.format(count)
		mc.file(rename = '{}/{}'.format(savepath, file_name))
		mc.file(s=True, type="mayaAscii")
		self.update_version()

	def publish(self):
		file = self.ui.Listfile.currentIndex().data(QtCore.Qt.UserRole)
		#self.capture.exec_()
		#print self.capture.action
		newfile = file.split('/')[-1]
		newfile = newfile.replace(file.split('_')[-1],'')
		publish = file.split('\\')[0]
		publish = publish.replace("workspace", "publish")
		allfile = os.listdir(publish)
		if 'Hero' not in allfile:
			os.mkdir('{}/Hero'.format(publish))
			allfile = os.listdir(publish)
		shutil.copyfile(file,'{}/Hero/{}hero.ma'.format(publish, newfile))
		if self.capture.action == 'capture':
			imageSnapshot = '{}/Hero/{}hero_Snapshot.jpg'.format(publish, newfile)
			mc.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
		count = len(allfile)
		os.mkdir('{}/V{:03d}'.format(publish, count))
		shutil.copyfile(file,'{}/V{:03d}/{}V{:03d}.ma'.format(publish, count, newfile, count))
		if self.capture.action == 'capture':
			imageSnapshot = '{}/V{:03d}/{}V{:03d}_Snapshot.jpg'.format(publish, count, newfile, count)
			mc.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
		check = file.split('/')
		filters = [['name', 'is', self.ui.project_combo.currentText()]]
		project = sg.find_one("Project", filters)
		if 'asset' in check:
			filters = [['project', 'is', project], ['code', 'is', self.ui.Listitem.currentItem().text()]]
			asset = sg.find_one('Asset', filters)
			filters = [['entity', 'is', asset], ['content', 'is', self.ui.Task_combo.currentText()]]
			task = asset = sg.find_one('Task', filters)
			if self.ui.update_combo.currentText() == 'Final':
				sg.update('Task', task['id'], {'sg_status_list' : 'fin'})
			else:
				sg.update('Task', task['id'], {'sg_status_list' : 'ip'})
		elif 'shot' in check:
			filters = [['project', 'is', project], ['code', 'is', self.ui.Listitem.currentItem().text()]]
			shot = sg.find_one('Shot', filters)
			filters = [['entity', 'is', shot], ['content', 'is', self.ui.Task_combo.currentText()]]
			task = asset = sg.find_one('Task', filters)
			if self.ui.update_combo.currentText() == 'Final':
				sg.update('Task', task['id'], {'sg_status_list' : 'fin'})
			else:
				sg.update('Task', task['id'], {'sg_status_list' : 'ip'})
class filename_ui(QtWidgets.QDialog):
	"""docstring for filename_ui"""
	def __init__(self, dirname, category, parent=None):
		super(filename_ui, self).__init__(parent=parent)
		self.cui = cui.ui_name()
		self.cui.setupUi(self)
		self.dirname = dirname
		self.category = category
		self.department_asset = ['Art', 'Character FX', 'Lookdevelop', 'Model', 'Rig']
		self.department_shot = ['Animation', 'VFX', 'Comp', 'Layout', 'Light']
		self.setWindowTitle('{} Name'.format(self.category))
		self.button()
	
	def button(self):
		self.cui.create.clicked.connect(self.returnpath)

	def returnpath(self):
		new_dirname = self.dirname+ '/' + self.cui.filename_edit.text()
		if self.category == 'project':
			os.mkdir(new_dirname)
			os.mkdir('{}/asset'.format(new_dirname))
			filters = [['code', 'is', 'Asset']]
			task_template = sg.find("TaskTemplate", filters)
			filters = [['task_template', 'is', task_template]]
			fields =['content', 'task_template', 'step']
			taskall = sg.find("Task", filters, fields)
			for asset in self.department_asset:
				os.mkdir('{}/asset/{}'.format(new_dirname, asset))
				for task in taskall:
					if task['step']['name'] == asset:
						os.mkdir('{}/asset/{}/{}'.format(new_dirname, asset, task['content']))
			os.mkdir('{}/shot'.format(new_dirname))
			filters = [['code', 'is', 'Shot']]
			task_template = sg.find("TaskTemplate", filters)
			filters = [['task_template', 'is', task_template]]
			fields =['content', 'task_template', 'step']
			taskall = sg.find("Task", filters, fields)
			for shot in self.department_shot:
				os.mkdir('{}/shot/{}'.format(new_dirname, shot))
				for task in taskall:
					if task['step']['name'] == shot:
						os.mkdir('{}/shot/{}/{}'.format(new_dirname, shot, task['content']))
			app.update_project()
			filters = [["name","is","Animation Template"]]
			project = sg.find_one("Project", filters)
			project_data = {'name': self.cui.filename_edit.text(), 'layout_project': project}
			sg.create('Project', project_data)

		elif self.category == 'department':
			check = self.dirname.split("/")
			if 'Asset' in check:
				filters = [['entity_type', 'is', 'Asset'],['code', 'is', self.cui.filename_edit.text()]]
				steps = sg.find("Step", filters)
				if steps == []:
					data = {'code': self.cui.filename_edit.text(), 'entity_type': 'Asset'}
					sg.create('Step', data)
			elif 'Shot' in check:
				filters = [['entity_type', 'is', 'Shot'],['code', 'is', self.cui.filename_edit.text()]]
				steps = sg.find("Step", filters)
				if steps == []:
					data = {'code': self.cui.filename_edit.text(), 'entity_type': 'Shot'}
					sg.create('Step', data)
			os.mkdir(new_dirname)
			app.update_deparment()
		
		elif self.category == 'task':
			filters = [['name', 'is', app.ui.project_combo.currentText()]]
			project = sg.find_one("Project", filters)
			check = self.dirname.split("/")
			filters = [['code', 'is',app.ui.department_combo.currentText()]]
			step = sg.find_one('Step', filters)
			if 'asset' in check:
				filters = [['project', 'is', project]]
				fields = ['code']
				assets = sg.find("Asset", filters, fields)
				os.mkdir(new_dirname)
				filters = [['code', 'is', 'Asset']]
				task_template = sg.find_one("TaskTemplate", filters)
				data = {'content' : self.cui.filename_edit.text(),
							'step' : step,
							'task_template' : task_template
					}
				sg.create('Task', data)
				for asset in assets:
					sg.update('Asset', asset['id'], {'task_template' : None})
					sg.update('Asset', asset['id'], {'task_template' : task_template})
					os.mkdir('{}/{}'.format(new_dirname, asset['code']))
			elif 'shot' in check:
				filters = [['project', 'is', project]]
				fields = ['code']
				shots = sg.find("Shot", filters, fields)
				os.mkdir(new_dirname)
				filters = [['code', 'is', 'Shot']]
				task_template = sg.find_one("TaskTemplate", filters)
				data = {'content' : self.cui.filename_edit.text(),
							'step' : step,
							'task_template' : task_template
					}
				sg.create('Task', data)
				for shot in shots:
					sg.update('Shot', shot['id'], {'task_template' : None})
					sg.update('Shot', shot['id'], {'task_template' : task_template})
					os.mkdir('{}/{}'.format(new_dirname, shot['code']))
			app.update_task()
		
		elif self.category == 'item':
			asset_path = app.ui.AssetorShot.itemData(app.ui.AssetorShot.currentIndex(), QtCore.Qt.UserRole)
			department_list = os.listdir(asset_path)
			filters = [['name', 'is', app.ui.project_combo.currentText()]]
			project = sg.find_one("Project", filters)
			check = self.dirname.split("/")
			if 'asset' in check:
				filters = [['code', 'is', 'Asset']]
				template = sg.find_one("TaskTemplate", filters)
				asset_data = {'code': self.cui.filename_edit.text(),
							  'task_template': template,
							  'project': project}
			  	sg.create('Asset', asset_data)
			elif 'shot' in check:
				filters = [['code', 'is', 'Shot']]
				template = sg.find_one("TaskTemplate", filters)
				shot_data = {'code': self.cui.filename_edit.text(),
							  'task_template': template,
							  'project': project}
			  	sg.create('Shot', shot_data)
			for department in department_list:
				all_task = os.listdir(asset_path+'/'+department)
				for task in all_task:
					asset_dir = '{}/{}/{}/{}'.format(asset_path, department, task,self.cui.filename_edit.text())
					os.mkdir(asset_dir)
					os.mkdir('{}/publish'.format(asset_dir))
					os.mkdir('{}/workspace'.format(asset_dir))
			
			app.update_item()
		self.deleteLater()
'''class Capture(QtWidgets.QDialog):
	clicked = QtCore.Signal(object)
	def __init__(self, parent=None):
		super(Capture, self).__init__(parent=parent)
		self.capui = capui.Ui_Capture()
		self.capui.setupUi(self)
		layout = mui.MQtUtil.fullName(long(getCppPointer(self.capui.verticalLayout)[0]))
		mc.setParent(layout)
		paneLayoutName = mc.paneLayout()
		ptr = mui.MQtUtil.findControl(paneLayoutName)
		self.paneLayout = wrapInstance(long(ptr), QtWidgets.QWidget)
		self.modelEditorname = mc.modelEditor(cam = 'persp',da = "smoothShaded")
		ptr = mui.MQtUtil.findControl(self.modelEditorname)
		self.modelEditor = wrapInstance(long(ptr), QtWidgets.QWidget)
		self.capui.viewport_layout.addWidget(self.paneLayout)
		self.button()
	
	def button(self):
		self.capui.pushButton.clicked.connect(self.capture)
	
	def capture(self):
		self.action = 'capture'
		self.close()'''


def show():
	global app
	try:
		app.deleteLater()
	except:
		pass
	app = Mainapp(getMayaWindow())
	app.show()

def getMayaWindow(): 
	ptr = mui.MQtUtil.mainWindow()
	return wrapInstance(long(ptr), QtWidgets.QWidget)
