#!/bin/bash

#for x in /usr/share/icons/Humanity/mimes/48/*; do inkscape -f /usr/share/icons/Humanity/mimes/48/zip.svg -e zip.png;done

for x in *.png
do
    y=$(basename "$x" .png)
    echo ".ficon.$y{background-image:url('mimetypes/$y.png');}"
done

