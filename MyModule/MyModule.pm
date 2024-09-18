package MyModule::MyModule;
use Exporter qw(import);
our @EXPORT = qw(get_array get_num get_num2 get_list custom_list get_dictionary); 

sub get_num {
    return 42;
}

sub get_array {
    my @array = ("apple", "banana", "cherry");
    return @array;
}

sub get_num2 {
    return 50;
}

sub get_list {
    my @list = (1, 29, "red", "blue");
    return @list;
}

sub custom_list {
    my @list = ($ARGV[0], $ARGV[1], int($ARGV[2]), $ARGV[3]);
    return @list;
}

sub get_dictionary {
    my %dictionary = (
    "apple"  => "A fruit that is usually red, green, or yellow",
    "banana" => "A long, curved fruit that is yellow when ripe",
    "carrot" => "A root vegetable, usually orange in color",);
    $dictionary{"date"} = "A sweet fruit that is typically brown";
    return %dictionary;
}

1;
