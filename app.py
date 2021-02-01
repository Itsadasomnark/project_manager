import maya.cmds as mc
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from shiboken2 import wrapInstance
import os, time
import json
import shutil

import ui 
reload(ui)
import createUI as cui
reload(cui)

global path
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
		self.ui.department_combo.currentIndexChanged.connect(self.update_task)
		self.ui.newproject.clicked.connect(self.create_project)
		self.ui.path_Button.clicked.connect(self.get_path)
		self.ui.workspace.toggled.connect(self.update_item)
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

	def get_path(self):
		fileDir = QtWidgets.QFileDialog.getExistingDirectory()
		with open('{}/root/root.json'.format(self.path_module), 'w') as jsonfile:
			json.dump(fileDir, jsonfile,sort_keys=True,indent=4)
		global path
		path = fileDir
		self.update_project()
		self.update_deparment()
		self.ui.textEdit.setText(fileDir)
	
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
			self.ui.Task_combo.currentIndexChanged.emit(True)
		self.ui.Task_combo.currentIndexChanged.emit(True)

	def update_item(self):
		task = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole)
		if task != None:
			if self.ui.workspace.isChecked() == True:
				task += '/workspace'
				self.ui.save.setDisabled(False)
				self.ui.publish_button.setDisabled(False)
			else:
				task += '/publish'
				self.ui.save.setDisabled(True)
				self.ui.publish_button.setDisabled(True)
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
		listitem = self.ui.Listitem.currentIndex().data(QtCore.Qt.UserRole)
		if self.ui.workspace.isChecked() == True: 
			self.ui.version_combo.clear()
			self.ui.Listfile.clear()
			for (root, dirs, files) in os.walk(listitem, topdown=True):
				for file in files:
					item = QtWidgets.QListWidgetItem()
					item.setText(file)
					fullpath = '{}/{}'.format(root,file)
					item.setData(QtCore.Qt.UserRole, fullpath)
					self.ui.Listfile.addItem(item)
		else:
			allversion = os.listdir(listitem)
			self.ui.version_combo.blockSignals(True)
			self.ui.version_combo.clear()
			self.ui.version_combo.addItems(allversion)
			for version in range(len(allversion)):
				fullpath = '{}/{}'.format(listitem,allversion[version])
				self.ui.version_combo.setItemData(version, fullpath, QtCore.Qt.UserRole)
			self.ui.version_combo.blockSignals(False)
			self.ui.version_combo.currentIndexChanged.emit(True)

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
		create = filename_ui(dirname, 'project')
		try:
			create.close()
		except:
			pass
		create.show()

	def create_department(self):
		global create
		dirname = self.ui.project_combo.itemData(self.ui.project_combo.currentIndex(), QtCore.Qt.UserRole)
		dirname += '/{}'.format(self.ui.AssetorShot.currentText())
		create = filename_ui(dirname, 'department')
		try:
			create.close()
		except:
			pass
		create.show()

	def create_task(self):
		global create
		dirname = self.ui.department_combo.itemData(self.ui.department_combo.currentIndex(), QtCore.Qt.UserRole)
		create = filename_ui(dirname, 'task')
		try:
			create.close()
		except:
			pass
		create.show()

	def create_item(self):
		global create
		dirname = self.ui.Task_combo.itemData(self.ui.Task_combo.currentIndex(), QtCore.Qt.UserRole)
		create = filename_ui(dirname, 'item')
		try:
			create.close()
		except:
			pass
		create.show()
	
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
		savepath = self.ui.Listitem.currentIndex().data(QtCore.Qt.UserRole)
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
		newfile = file.split('/')[-1]
		newfile = newfile.replace(file.split('_')[-1],'')
		publish = file.split('\\')[0]
		publish = publish.replace("workspace", "publish")
		allfile = os.listdir(publish)
		if 'Hero' not in allfile:
			os.mkdir('{}/Hero'.format(publish))
			allfile = os.listdir(publish)
		shutil.copyfile(file,'{}/Hero/{}hero.ma'.format(publish, newfile))
		count = len(allfile)
		os.mkdir('{}/V{:03d}'.format(publish, count))
		shutil.copyfile(file,'{}/V{:03d}/{}V{:03d}.ma'.format(publish, count, newfile, count))

class filename_ui(QtWidgets.QMainWindow):
	"""docstring for filename_ui"""
	def __init__(self, dirname, category, parent=None):
		super(filename_ui, self).__init__(parent=parent)
		self.cui = cui.ui_name()
		self.cui.setupUi(self)
		self.dirname = dirname
		self.category = category
		self.department_asset = ['Design', 'Groom', 'Lookdevelop', 'Model', 'Rig']
		self.department_shot = ['Animation', 'CFX', 'Composit', 'Layout', 'Lighting', 'VFX']
		self.setWindowTitle('{} Name'.format(self.category))
		self.button()
	
	def button(self):
		self.cui.ok.clicked.connect(self.returnpath)

	def returnpath(self):
		new_dirname = self.dirname+ '/' + self.cui.name.text()
		if self.category == 'project':
			os.mkdir(new_dirname)
			os.mkdir('{}/asset'.format(new_dirname))
			for asset in self.department_asset:
				os.mkdir('{}/asset/{}'.format(new_dirname, asset))
			os.mkdir('{}/shot'.format(new_dirname))
			for shot in self.department_shot:
				os.mkdir('{}/shot/{}'.format(new_dirname, shot))
			app.update_project()
		elif self.category == 'department':
			os.mkdir(new_dirname)
			app.update_deparment()
		elif self.category == 'task':
			os.mkdir(new_dirname)
			os.mkdir('{}/publish'.format(new_dirname))
			os.mkdir('{}/workspace'.format(new_dirname))
			app.update_task()
		elif self.category == 'item':
			os.mkdir('{}/publish/{}'.format(self.dirname, self.cui.name.text()))
			os.mkdir('{}/workspace/{}'.format(self.dirname, self.cui.name.text()))
			app.update_item()
		self.deleteLater()
def show():
	global app
	try:
		app.deleteLater()
	except:
		pass
	app = Mainapp(getMayaWindow())
	app.show()


def getMayaWindow(): 
	import maya.OpenMayaUI as mui
	ptr = mui.MQtUtil.mainWindow()
	return wrapInstance(long(ptr), QtWidgets.QWidget)
