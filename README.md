<p align="center">
	<a href="https://www.python.org/" target="_blank" alt="Picture of python with link to python.org">
        	<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">
	</a> 
	<a herf="https://www.json.org/json-en.html" target="_blank" alt="Picture of json with link to json.org">
		<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white">
	</a>
 	<hr />
</p>

# CMBFan

***WARNING! THIS PROGRAM IS A WORK IN PROGRESS! ANYTHING CAN CHANGE AT ANY MOMENT WITHOUT ANY NOTICE! USE THIS PROGRAM AT YOUR OWN RISK!***

### CM I/O Board Fan Control

It's a program for the [Compute Module 4 I/O Board](https://www.raspberrypi.com/products/compute-module-4-io-board/) to control the pwm port over i2c bus interface. You can read all further information about cibfan, below.

### Why?

In January 2022, I bought a Pi Compute Module 4 and belonging to it, Compute Module I/O board as well as suitable housing. I have a small fan in this case, this can be connected by PWM to the Compute Module I/O board, but then you can control it only by [cli i2c commands](https://linux.die.net/man/8/i2cget).

My basic goal is, to create a program that runs on as far as every Linux system and loads user settings via a file with maybe some special additonal features like stresstest.


### Features & Targets:

- [x] Logging
- [ ] User settings (load via file)
- [ ] Background process
- [ ] Automatic installation
- [ ] Output of diagrams (curves (possibly picture)) of the temperature course

### ToDo

- [x] README.md
- [x] Select language (in first step, i wanna try [Python3.10](https://www.python.org/downloads/) 
- [x] First structure & Main program files to test.
- [ ] Read/set (temp), speed
- [ ] Background process (start @boot and set default user config (systemd?))
- [ ] Install script (deb?)
- [ ] Output of diagrams (curves)
- [ ] Optimized
- [ ] Update readme.me more and more.

### Issue's & Discuss

If you use this program, please keep in mind that it is in work in process. Serious errors may occur. You can file a bug report [here](https://github.com/iptoux/CMBFan/issues) (please check first if there is already a bug/issue/incident). 

Thanks :slightly_smiling_face:

You are invited in this comunity and can creat or follow any discussion [here](https://github.com/iptoux/CMBFan/discussions)