# Auto Open Daily Required Applications with Windows Task Scheduler and Set Up them

This Repo have Simulation of chrome we can do the same process for other applications also...

## Steps For adding any task in Windows Task Scheduler :-

1) In windows search panel search for "task scheduler" and select application "Task Scheduler", will open window as follows.
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211763643-9c201136-171f-4aa7-9f92-77801f1de43e.png"/>
</p>
2) Right Click on Task Scheduler Library and create new folder to keep our custom startup scripts different from system ones...
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211764104-5386dfeb-9734-445f-a13c-0bc750af217d.png"/>
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211764239-edb676cb-22dd-43f7-a977-2d048e6a5234.png"/>
</p>
3) Now in Task Sheduler Library shows our newly created folder right click on it and select 'create basic task'
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211764902-cfcb0006-40a1-4469-85b0-728d00c60d81.png"/>
</p>
4) Will open  up  following  window,  add respective name and click next
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211765164-f0d610e6-066d-4b32-8be8-08442aca1ba0.png"/>
</p>
5) In next step we have to choose triggers according  to requirement,
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211765404-4134c4d1-8a88-4c2b-8599-3414d21cf25f.png"/>
</p>
6) on next it will show start time of task and respective date and recur every day/month/weekly according to your previous choice, click on next
7) Here we get following options we can choose accoording to our need, we choose option 'start program' for our script
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211765940-c86fae75-0c76-46ac-8c1b-6299922445ec.png"/>
</p>
8) On This step it will ask path to script we can add path or use browse option, along with arguments.
<p align="center">
  <img src="https://user-images.githubusercontent.com/61587515/211766458-5501fa18-9324-4fd4-93c8-d474c885ce95.png"/>
</p>
9) Subsequently it will show all details about task, we can click on finish to complete process and Done. We have Successfully sheduled task.

### Instead of Windows Task Scheduler we can also use a bat file to make job done but it makes we have run bat file to run all tasks...!!

```bat
"DRIVE NAME HERE IF YOU HAVE SCRIPT IN DIFFERENT FOLDER FOR EXAMPLE :- 'G:'"
chcp 65001>nul
cd "PATH_TO_SCRIPT_FOLDER"
@echo off
py -u "start.py"
timeout /t 10 >nul
```
