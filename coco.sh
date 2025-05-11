co () {
    if [[ -z "$1" ]]; then
        echo "Usage: co <number_of_instances>"
        return 1
    fi

    pkill -f coco.py
#    venv #or: source ~/path/to/venv/bin/activate

    pwd=$(pwd)

    for i in $(eval echo {1..$1})
    do
        python coco.py >> "coco_$i.log" 2>&1 &
        sleep 3s
    done

    cd "$pwd"
}

coco () {
    co "$1" &
}

cocon () {
    pkill -f coco.py
}

