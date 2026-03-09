from .any_alarm import AnyAlarm

NODE_CLASS_MAPPINGS = {
    "AnyAlarm": AnyAlarm,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnyAlarm": "🔔 any_alarm",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']