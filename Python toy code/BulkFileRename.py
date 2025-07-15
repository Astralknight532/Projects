# Python bulk file rename
from os import listdir, rename # used for accessing files
from os.path import getctime # used for getting file creation time
from time import ctime, strptime, strftime # used for date & time operations

def main():
	folder = input("Enter a full path to a folder: ").replace("\\", "/")
	
	for count, filename in enumerate(listdir(folder)):
		unformatted_createtime = strptime(ctime(getctime(f"{folder}/{filename}")))
		formatted_createtime = strftime("%Y-%m-%d", unformatted_createtime)
		dst = f"[{formatted_createtime}]{filename}"
		src = f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst = f"{folder}/{dst}"
		if "[" in filename and "]" in filename:
			continue
		# rename() function will rename all the files
		rename(src, dst)
		#print(dst)

if __name__ == '__main__':
	main()