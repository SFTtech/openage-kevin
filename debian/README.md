## image creation

create a fresh debian sid image with openage dependencies

```
./build.py -f
```

## attaching

create a new throwaway container from the image and run `bash` interactively:

```
su - justin -c 'podman run --rm -i -t sft/openage:sid /bin/bash'
```
