# Virus-Detection-and-Anti-virus-Detection-in-Python
 
 ## **Abstract** ##
People use computers for all kinds of activities: online games, shopping, entertainment, emails, social media, study, research, etc. At the same time, the risk of infection with malicious software on these computers is also increasing. The big problem is that ordinary users do not understand what the virus is and how computers are infected. Although there are many vendors who produce antivirus software with various features to prevent or remove these viruses, ordinary users do not understand the concept of each feature in these programs and there is no tool to advise users on what the features mean and help them choose the right software for personal or business needs.The aim of this project is to create an anti-virus system with a variety of functions and features that can provide better information to users about how to deal with these situations in the current digital enhanced world. A virus program will also be developed to highlight all the key features of the virus protection system.

## **Introduction** ##
In the world of computers and the Internet, it is important to be different from what you do unless you want to get into a bad piece of code that could hinder your performance or simply turn your computer or device into a spy program. To find out more let's find out the official definitions of viruses and their anti-viruses and their meses. A virus is a dangerous code that is uploaded to your device for the purpose of causing damage and theft. Computer viruses replicate and absorb all available memory and cause systemic crashes. Some viruses can replicate and transmit their copies across all networks and bypass security programs. Protecting your computer or network - an anti-virus program is required.Regular antivirus software scans, detects and removes viruses, computer worms, Trojans, etc. Most anti-virus programs are aware of the automatic update feature so you can keep up to date with the latest virus definitions being released worldwide. They offer desirable and available scanning options where available and options vary from user to user. Here we aim to mimic a viral attack, prevention and treatment.

## **Existing Systems** ##

The computer that we use now has become an indispensable component of our daily lives. Without them, our daily tasks, as well as our vocations, would be nearly impossible. We also sought to ensure safety and privacy when utilizing them, notably from malware. Antivirus software is designed to prevent viruses from infecting your computer. Our machine will be vulnerable to viruses and other threats if you don't have an antivirus programme installed. Apart from eradicating infections, antivirus software has a number of other advantages. Antivirus software must be installed on all desktop computers, whether they are used at home or in the office. Users may experience disadvantages when utilizing them.

### Advantages and Disadvantages of anti-virus software’s: ###
![image](https://user-images.githubusercontent.com/88433888/199059354-9de21afc-f294-4809-a117-e8364151dfab.png)

## **Methodology** ##

### Virus System : ###

The virus program will be a program that will infect the victim's file and copy its code to the file. This will create a recurring virus as the code is repeatedly copied.

### Infection Prevention Program : ###

The program has two modes for detecting an infected file - Easy Signature Recovery & Variation of size differences. The hash signatures are downloaded and updated to the system and further the program has a list of functions such as - Scanning, Blocking, Full Scanning etc. the user can use it to keep his device safe.

## **Modules or Tasks** ##

### Repetitive virus : ###

A virus that infects and copies itself into all files in the folder in which it is used.

### Easy Signature Recovery : ###

This is the module in which we detect whether a file has been infected by any known virus.

### Changing the Recovery Size : ###

When the virus code copies itself to any file the victim's file size increases. This is evident in the work.

### Update Hash Signature : ###

We download a well-known virus hash signature for the antivirus to identify and take the necessary steps against it.

### Scan : ###

Any file can be scanned to detect threats using this function.

### Hash File Conversion : ###

Does not show a threat if there is no virus. It indicates a threat if a virus is present.

### Add to Lock : ###

Any suspected file can be added to the lock folder

### Deleting Detained Files : ###

We can delete the locked files individually if it appears necessary.

### Restoring Quarantine Files : ###

We can restore any closed file if it appears to be harmless or unnecessary.

## **Flow Charts** ##

### Case 1 ###
![image](https://user-images.githubusercontent.com/88433888/199061341-7cd9239e-c92d-4f81-afb3-60227623db4b.png)

The scan program checks for the change in file sizes, the initial scan details with the final scan details. If the scan detects the change in file sizes it shows us which files had their file sizes changed i.e., infected. Then we have to delete those files, so that whenever we open that particular infected file, the virus won’t replicate itself again.

### Case 2###
![image](https://user-images.githubusercontent.com/88433888/199061518-3c8f7f70-2d6c-4f25-8209-aa2bc7b157a2.png)

The scan function checks the hashes with the updated list of hashes, if any hash of a file is found to be the same then the file is quarantined which is later deleted. If any hashes are not found the same it displays a message “no threat found”.

## **Architecture Diagram** ##
![image](https://user-images.githubusercontent.com/88433888/199061706-aa76a9c2-2a59-49ae-9d75-ed48b3ace688.png)

## **Output Screenshots** ##

This virus folder contains scan, victim and virus python code files.

![image](https://user-images.githubusercontent.com/88433888/199062120-345ce914-1499-4c4a-bde5-800df034be3a.png)

Victim file before getting infected with virus code

![image](https://user-images.githubusercontent.com/88433888/199062237-18948c4c-f612-4b16-9c56-6b0b27e26886.png)

Initial scan data of the files contained in the folder

![image](https://user-images.githubusercontent.com/88433888/199062319-cac6cec9-65e7-4cf4-962d-ac9c9fd61873.png)

The output for the virus file after executing

![image](https://user-images.githubusercontent.com/88433888/199062420-6c388df1-0009-4ed0-8a00-cb9b939417e7.png)


Victim file after getting infected with virus code(Virus replicated itself)

![image](https://user-images.githubusercontent.com/88433888/199062516-aa409a4f-0f72-456d-99d4-094e387e0418.png)

Output of the victim file when it is executed

![image](https://user-images.githubusercontent.com/88433888/199062611-e50b75a3-154f-4c2e-9236-285d235d7148.png)

Now we need to execute the scan file

![image](https://user-images.githubusercontent.com/88433888/199062678-fa954907-4948-4b9c-a305-4106ab172b2b.png)

We can see the changes in size before and after scanning in victim file 

### Antivirus folder : ###

![image](https://user-images.githubusercontent.com/88433888/199062881-cfe815fe-58af-411c-8f89-a031696c9bda.png)

### Antivirus GUI ###

![image](https://user-images.githubusercontent.com/88433888/199063001-16ac0c1d-1e05-4262-818d-809b94f97520.png)

### Scan ###

If the program detects virus in a particular file, it will be sent to quarantine from where we can delete the affected file.

![image](https://user-images.githubusercontent.com/88433888/199063138-b568205d-c0a2-4d9a-9218-c3fe3379e3ef.png)

Now here one threat is found and that threat will sent to Quarantine.

### Quarantine ###

![image](https://user-images.githubusercontent.com/88433888/199063310-a23f10e4-5f09-4baf-959c-19a90896fb5a.png)

The virus affected files are sent into quarantine where we can check and delete the affected file,we can also restore 	files from quarantine ,if required.

## **Conclusion** ##

Both virus and antivirus programs have been shown to be effective. The virus's recurrent feature is displayed. All of the antivirus program's basic but important capabilities have been implemented and can be used by anyone. Users can easily operate the system with a simple GUI, even if they have no prior knowledge of how antivirus software works. We learned a lot about cyber security and how to cope with potential dangers from bad websites and criminals as a result of this project. There will always be a need for white hat hackers to intervene and prevent bad individuals from stealing or exploiting data, as there will always be bad people seeking to steal or exploit data. We learned more about the formation and detection of viruses by going through many research papers, and that viruses are among the most dangerous threats to the internet world in the daily lives of many people across the world.










