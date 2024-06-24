# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from isaacsim import SimulationApp

# This sample enables a livestream server to connect to when running headless
CONFIG = {
    "width": 1280,
    "height": 720,
    "window_width": 1920,
    "window_height": 1080,
    "headless": True,
    "hide_ui": False,  # Show the GUI
    "renderer": "RayTracedLighting",
    "display_options": 3286,  # Set display options to show default grid
}


# Start the omniverse application
kit = SimulationApp(launch_config=CONFIG)

from omni.isaac.core.utils.extensions import enable_extension

# Default Livestream settings
kit.set_setting("/app/window/drawMouse", True)
kit.set_setting("/app/livestream/proto", "ws")
kit.set_setting("/ngx/enabled", False)

# Note: Only one livestream extension can be enabled at a time

# Enable Native Livestream extension
# Default App: Streaming Client from the Omniverse Launcher
# enable_extension("omni.kit.streamsdk.plugins-3.2.1")
# enable_extension("omni.kit.livestream.core-3.2.0")
# enable_extension("omni.kit.livestream.native")

# Enable WebRTC Livestream extension
# Default URL: http://localhost:8211/streaming/webrtc-client/
enable_extension("omni.services.streamclient.webrtc")


from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import numpy as np
world = World()
fancy_cube =  world.scene.add(DynamicCuboid(prim_path="/World/random_cube", name="fancy_cube", position=np.array([0, 0, 1.0]), scale=np.array([0.5015, 0.5015, 0.5015]), color=np.array([0, 0, 1.0]),)) # type: ignore
world.reset()

# Run until closed
while kit._app.is_running() and not kit.is_exiting():
    # Run in realtime mode, we don't specify the step size
    kit.update()
    # kit.step(render=True) # execute one physics step and one rendering step
    print("Cube position is : " + str(fancy_cube.get_world_pose()[0]), "Cube's linear velocity is : " + str(fancy_cube.get_linear_velocity()))

kit.close()
