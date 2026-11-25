import launch

if not launch.is_installed("aiohttp"):
    launch.run_pip("install aiohttp", "requirements for sd-forge-model-manager")

if not launch.is_installed("Pillow"):
    launch.run_pip("install Pillow", "requirements for sd-forge-model-manager")

if not launch.is_installed("send2trash"):
    launch.run_pip("install send2trash", "requirements for sd-forge-model-manager")
