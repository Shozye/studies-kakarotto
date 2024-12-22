#!usr/bin/perl

use HTTP::Daemon;
use HTTP::Status;  
#use IO::File;

my $d = HTTP::Daemon->new(
        LocalAddr => 'localhost',
        LocalPort => 4321,
    )|| die;

print "Please contact me at: <URL:", $d->url, ">\n";


while (my $c = $d->accept) {
    while (my $r = $c->get_request) {
        if ($r->method eq 'GET') {
            my $header = $r->headers->as_string;
            my $filename = "./index.html";
            open(FH, '>', $filename) or die $!;
            print FH $header;
            $file_s= "./index.html";    # index.html - jakis istniejacy plik
            close(FH);
            $c->send_file_response($file_s);

        }
        else {
            $c->send_error(RC_FORBIDDEN)
        }

    }
    $c->close;
    undef($c);
}