
class PauseUntilToggleOn:
    """
    Outputs the given image only if the toggle is True. Otherwise, outputs None.
    """
    RETURN_TYPES = ("IMAGE", None)
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", ),
                "toggle": ("INT", {"default": 0}),
            }
        }

    FUNCTION = "pause_on_toggle"
    CATEGORY = "utils"
    custom_name = "Pause Until Toggle On"

    def pause_on_toggle(self, image, toggle):
        if toggle == 1:
            return (image,)

    


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "PauseUntilToggleOn": PauseUntilToggleOn,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PauseUntilToggleOn": "Pause Until Toggle On",
}
