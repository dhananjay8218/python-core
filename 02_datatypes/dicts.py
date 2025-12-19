# Chapter 10: Dictionary operations
task_info = dict(name="Backup", status="Pending", priority=2)
print("Task info:", task_info)

task_config = {}
task_config["mode"] = "auto"
task_config["interval"] = "daily"

print("Mode:", task_config["mode"])
print("Config:", task_config)

del task_config["interval"]
print("Config:", task_config)

print("Contains priority?", "priority" in task_info)

task_info = {"name": "Sync", "status": "Running", "priority": 1}

removed_item = task_info.popitem()
print("Removed:", removed_item)

extra_options = {"retry": "enabled", "timeout": "30s"}
task_config.update(extra_options)

print("Updated config:", task_config)

note = task_info.get("status", "NO STATUS")
print("Note:", note)
