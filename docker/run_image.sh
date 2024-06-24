xhost +
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." && pwd )"

docker run --name isaac-sim-4-0-0 --entrypoint bash -it --gpus all -e "DISPLAY=:1" -e "ACCEPT_EULA=Y" -e "OMNI_SERVER=omniverse://<ip>/NVIDIA/Assets/Isaac/4.0" --rm --network=host \
    -v ~/docker/isaac-sim/kit/cache/Kit:/isaac-sim/kit/cache:rw \
    -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
    -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
    -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/documents:/root/Documents:rw \
    -v "$ROOT_DIR":/root/workspace \
    -p 2200:22 \
    -e ROS_MASTER_URI=http://localhost:11311 \
    --privileged \
    nvcr.io/nvidia/isaac-sim:4.0.0


