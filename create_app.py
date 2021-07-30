import  os
import time 
file_name = input('Enter main py file name with .py ---> ')

create_setup_file = 'py2applet --make-setup {}'.format(file_name)
delete_ = 'rm -rf build dist'
alias_ = 'python3 setup.py py2app -A'
deploy = 'python3 setup.py py2app'

command_list = [create_setup_file, delete_, alias_, deploy]  
if __name__ == '__main__':
	file_name
	for i in command_list:
		time.sleep(2)
		os.system(i)
