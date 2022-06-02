## Task nr 5 - HTTP
File server3.pl contains example program of a server protocol HTTP.  

1. Execute the script, test and think how it works.
2. Establish connection using web browser.
3. Change script or write your own server, that sends back request header.
4. Change script (or write your own server in any programming language) to manage client requests to simple text WWW service (few static websites with static links to each other) saved in some folder on local disc of user.
5. Intercept communicates to/from server using any analyser - Analyse their structure
6. Write simple report.

Server:
```perl
  use HTTP::Daemon;
  use HTTP::Status;  
  #use IO::File;

  my $d = HTTP::Daemon->new(
           LocalAddr => 'lukim',
           LocalPort => 4321,
       )|| die;
  
  print "Please contact me at: <URL:", $d->url, ">\n";


  while (my $c = $d->accept) {
      while (my $r = $c->get_request) {
          if ($r->method eq 'GET') {
              $file_s= "./index.html";    # index.html - jakis istniejacy plik
              $c->send_file_response($file_s);

          }
          else {
              $c->send_error(RC_FORBIDDEN)
          }

      }
      $c->close;
      undef($c);
  }
```
1. To test it we have to change `local address` to `localhost` and then create file `index.html`. It is advisable to add `#!usr/bin/perl` on the beginning of file. Run the program using 
```bash
perl server3.pl
```
2. Then on the address `http://127.0.0.1:4321/` we will be able to see contents of index.html
3. To better understand what's written in Perl look [here](https://metacpan.org/pod/HTTP::Daemon)  
To send back request header we need to insert header into the `index.html` or create other file and change `$file_s`  
To get header I used [this](https://stackoverflow.com/questions/49038859/how-to-get-full-http-request-not-response-headers)  
Then write to file using [this](https://www.perltutorial.org/perl-write-to-file/)  
End result is in `./zad3_server3.pl`
4. Let's make Example website structure:
```bash
index.html hyperlinks:
- main.html
- catalog.html
- contact.html
- index.html
- folder/idk.html

main.html and catalog.html and contact.html and idk.html hyperlinks:
- index.html
```
in `$r->uri` we can get parameters of url request.
```perl
if($r->uri eq "/" | $r->uri eq "/favicon.ico"){
    my $file_s = "./ExampleWebsite/index.html";
    $c->send_file_response($file_s);
} else{
    $file_s = $dir.$r->uri;
    $c->send_file_response($file_s);
}
```
If is needed to figure out if user is connecting to the website for the first time.  
5. Run wireshark with `sudo wireshark`
Then click on `Loopback: lo`. This is where packets will show up.
![packets](/wireshark_packets.png)
We can see there Packets with port 4321 -> 57582. This is communication between client and server. 
Get messages contain Header or website content.