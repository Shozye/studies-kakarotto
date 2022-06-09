#!usr/bin/perl

use HTTP::Daemon;
use HTTP::Status;  
use Data::Dumper;
$Data::Dumper::Terse = 1;
$Data::Dumper::Useqq = 1;

my $d = HTTP::Daemon->new(
        LocalAddr => 'localhost',
        LocalPort => 4321,
    )|| die;

print "Please contact me at: <URL:", $d->url, ">\n";

my $dir = "./ExampleWebsite";
while (my $c = $d->accept) {
    while (my $r = $c->get_request) {
        if ($r->method eq 'GET') {
            if($r->uri eq "/" | $r->uri eq "/favicon.ico"){
                my $file_s = "./ExampleWebsite/index.html";
                $c->send_file_response($file_s);
            } else{
                $file_s = $dir.$r->uri;
                $c->send_file_response($file_s);
            }
        }else {
            $c->send_error(RC_FORBIDDEN)
        }

    }
    $c->close;
    undef($c);
}