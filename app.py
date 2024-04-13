import torch

# Mevcut GPU sayısını ve adını alın
device_count = torch.cuda.device_count()
device_name = torch.cuda.get_device_name()

print("GPU Sayısı:", device_count)
print("GPU Adı:", device_name)

# Her GPU'nun bellek kapasitesini döngüyle alın
for i in range(device_count):
    gpu_properties = torch.cuda.get_device_properties(i)
    print(f"GPU {i} Bellek Kapasitesi: {gpu_properties.total_memory / (1024**3)} GB")
