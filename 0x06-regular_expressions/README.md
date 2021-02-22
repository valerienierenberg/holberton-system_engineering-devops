# 0x06-regular_expressions

## Project Description:
This project introduces the concept of Regular Expressions

## Background Context:
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```
$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
$
$ ./example.rb 127.0.0.2
127.0.0.2
$ ./example.rb 127.0.0.1
127.0.0.1
$ ./example.rb 127.0.0.a
```

## General Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
* All your regex must be built for the Oniguruma library


# File Descriptions:

* 0-simply_match_holberton.rb - The regular expression must match Holberton. Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method
* 1-repetition_token_0.rb - Find the regular expression that will match the above cases (provided in example image) Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method
* 2-repetition_token_1.rb - Find the regular expression that will match the above cases (provided in example image) Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method
* 3-repetition_token_2.rb - Find the regular expression that will match the above cases (provided in example image) Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method
* 4-repetition_token_3.rb - Find the regular expression that will match the above cases (provided in example image) Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method. Your regex should not contain square brackets.
* 5-beginning_and_end.rb - The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between.
Using the project instructions, create a Ruby script that accepts one argument, and pass it to a regular expression matching method.
* 6-phone_number.rb - This task is brought to you by Holberton professional advisor Neha Jain, Senior Software Engineer at LinkedIn.\
Requirement:\
The regular expression must match a 10 digit phone number\
Example:
```
$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
$ ./6-phone_number.rb " 4155049898" | cat -e
$
$ ./6-phone_number.rb "415 504 9898" | cat -e
$
$ ./6-phone_number.rb "415-504-9898" | cat -e
$
$
```

* 7-OMG_WHY_ARE_YOU_SHOUTING.rb - The regular expression must be only matching: capital letters
* 100-textme.rb - This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

* Your script should output: [SENDER],[RECEIVER],[FLAGS]
* The sender phone number or name (including country code if present)
* The receiver phone number or name (including country code if present)
* The flags that were used
* (log file provided)
\
* 101-passed_linkedin_regex_challenge.jpg - One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.
\
Requirements:
* Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle
Provide as an answer file a screenshot of the “Congratulations” screen with the date and time of completion
