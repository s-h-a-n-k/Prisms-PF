#!/bin/sh

location=$1
variable=$2
bound=$3
visitdir=$4
home=$HOME


if [ "$(expr substr $visitdir 1 1)" = "~" ]
then
    visitdir=$home$(expr substr $visitdir 2  $(expr ${#visitdir} - 1))
fi

visit="$visitdir -cli -s"

if [ "$(expr substr $location 1 1)" = "~" ]
then
    location=$home$(expr substr $location 2  $(expr ${#location} - 1))
fi
if [ "$(expr substr $location ${#location} 1)" != "/" ]
then
    location=$location/
fi

mkdir $location"Observations/"
slocation=$location"Observations/"

f="./Scripts/scripts/"

python $f"f_tot_vs_t.py" $location $slocation
$visit $f"domain_stats.py" "$location" "$bound" "$variable" "$slocation"
python $f"domain_count_vs_t.py" "$bound" "$slocation"
$visit $f"phase_fraction.py" "$location" "$variable" "$slocation"
python $f"phase_fraction_vs_t.py" $slocation
$visit $f"interface_area.py" "$location" "$variable" "$bound" "$slocation"
python $f"interface_area_vs_t.py" $slocation
python $f"get_data.py" "$location" "$bound" "$variable" "$slocation"

echo "Files saved in "$slocation
