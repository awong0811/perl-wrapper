BEGIN {
    use FindBin qw($Bin);
    use lib $FindBin::Bin;
}

use Getopt::Long qw(:config no_ignore_case);
use JSON;

use MyModule::MyModule;

GetOptions ('num' => \$num,
            'array' => \$array,
            'num2' => \$num2,
            'list' => \$list,
            'clist' => \$clist,
            'dict' => \$dict);

if ($num) {
    my $ret = get_num();
    print "$ret\n";
    # print to_json($ret);
}
elsif ($array) {
    my @array = get_array();
    print join(' ', @array), "\n";
}
elsif ($num2) {
    my $ret = get_num2();
    print to_json($ret);
}
elsif ($list) {
    my @list = get_list();
    print to_json(\@list);
}
elsif ($clist) {
    $num = $ARGV[0];
    $first = $ARGV[1];
    $second = $ARGV[2];
    $third = $ARGV[3];
    $fourth = $ARGV[4];
    my @list = custom_list($num, $first, $second, $third, $fourth);
    print to_json(\@list);
}
elsif ($dict) {
    my %dict = get_dictionary();
    print to_json(\%dict);
}