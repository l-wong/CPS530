#!/usr/bin/perl
use CGI ':standard';
print "Content-type: text/html\n\n";
print "<html> <head>\n";
print "<title> Lab 04 Part 2 CGI</title>\n";
print "<link href='https://fonts.googleapis.com/css?family=Share+Tech+Mono' rel='stylesheet'>\n";
print "<style>\n";
print "body { font-family: 'Share Tech Mono'; color: #4da6ff; font-size: 5em; text-align:center; background-color: #e6f2ff; } home { width:40px; height: 40px;}\n";

print "</style></head>\n";
print "<body>\n";
print "<div class='home'>\n";
print "<a href='http://www2.scs.ryerson.ca/~l86wong/lab04/lab04pt2.html'>\n";
print "<img src='http://2.bp.blogspot.com/-NXQU23dwa_U/U-jRl3DgiSI/AAAAAAAAGZo/e6BgxwvK59M/s184/unnamed.png'>\n";
print "</a>\n";
print "</div>\n";
@name = param('name');
$dog = param('dog');
$gender = param('gender');
print "Hello @name!\n\n";

if ($gender eq "Female")
  {
    print "You are a female, and \n";
  }
elsif ($gender eq "Male"){

  print "You are male, and \n";
}
else {
  print "You prefer not to say what gender, and \n";
}

if ($dog eq "Pug"){
  print "your favourite dog is a pug.\n\n";
  print "<img src='https://vignette.wikia.nocookie.net/videogames-fanon/images/7/72/Nintenpug%21%21%21.png/revision/latest?cb=20140323030107'>\n";
}

elsif ($dog eq "Husky"){
  print "your favourite dog is a husky.\n\n";
  print "<img src='https://i.pinimg.com/originals/1f/1d/23/1f1d23f5dba29ab7b2dd5b61fecc5e08.jpg'\n";

}

else {
  print "your favourite dog is a chihuahua.\n\n";
  print "<img src='https://www.chelseadogs.com/media/wysiwyg/shop-by-breed/chihuahua-xs.png'\n";
}


print "</body>\n";
print "</html>\n";
