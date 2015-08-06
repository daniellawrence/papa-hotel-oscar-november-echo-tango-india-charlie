papa-hotel-oscar-november-echo-tango-india-charlie
--------------------------------------------------

STDIN to phonetic


    ./phonetic.py --help
    usage: phonetic.py [-h] [--dialect {nato,nato-phonetic,evil}]
    optional arguments:
    -h, --help          show this help message and exit
    --dialect {nato,nato-phonetic,evil}
                        phonetci alphabet to use


Examples
--------------------

Default (NATO)

    echo 'hello world' | ./phonetic.py
    (hello) hotel echo lima lima oscar
    (world) whiskey oscar romeo lima delta

NATO super phonetic

    echo 'hello world' | ./phonetic.py --dialect nato-phonetic
	(hello) hoh-tel eck-oh lee-mah lee-mah oss-cah
	(world) wiss-key oss-cah row-me-oh lee-mah dell-tar

Evil

    echo 'hello world' | ./phonetic.py --dialect evil
	(hello) heir euphrates lima lima ouija
	(world) write ouija right lima django
 
