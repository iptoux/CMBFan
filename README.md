<p align="center">
      <a href="https://www.python.org/" target="_blank" alt="Picture with link to python.org">
        <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">
      </a>
  <hr />
</p>

# CMBFan

***WARNING! THIS PROGRAM IS A WORK IN PROGRESS! ANYTHING CAN CHANGE AT ANY MOMENT WITHOUT ANY NOTICE! USE THIS PROGRAM AT YOUR OWN RISK!***

### CM I/O Board Fan Control

It's a program for the [Compute Module 4 I/O Board](https://www.raspberrypi.com/products/compute-module-4-io-board/) to control the pwm port over i2c bus interface. You can read all further information about cibfan, below.

### Why?

In January 2022, I bought a Pi Compute Module 4 and belonging to it, Compute Module I/O board as well as suitable housing. I have a small fan in this case, this can be connected by PWM to the Compute Module I/O board, but then you can control it only by [cli i2c commands](https://linux.die.net/man/8/i2cget).

My basic goal is, to create a program that runs on as far as every Linux system and loads user settings via a file with maybe some special additonal features.

### Targets:

* Background process
* User settings (load via file)
* Automatic installation
* Output of diagrams (curves (possibly picture)) of the temperature course

### ToDo

- [x] README.md
- [ ] Update readme.me more and more.
- [ ] Select language (in first step, i wanna try [Python3.10](https://www.python.org/downloads/)
- [ ] Tests some ideas. 
- [ ] First structure
- [ ] Read/set (temp), speed
- [ ] Background progress (start @boot and set default user config (systemd?))
- [ ] Install script (deb?)
- [ ] Output of diagrams (curves)
- [ ] Native (ASM) compile NASM felf64
- [ ] Optimized

___
