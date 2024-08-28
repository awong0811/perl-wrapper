BEGIN {
    use lib '.';
}

use Getopt::Long qw(:config no_ignore_case);
use MyModule;


GetOptions ('num' => \$num,
            'array' => \$array);

if ($num) {
    my $num = MyModule::get_num();
    print "$num\n";
}
elsif ($array) {
    my @array = MyModule::get_array();
    print join(' ', @array), "\n";
}



