# LVM - управление логическими томами
3 абстракции:
PV (physical volume) - физические тома или целые разделы, в рамказ линукс это не важно
VG (volume group) - группа томов, объединяет один или несколько PV в группу образуя единое пространство из которого потом можно нарезать LV (логические тома)
LV (logical volume) - логические разделы, которые потом форматируются под нужную фс и монтируются в нужную папку

# Обычная задача. Увеличение диска виртуальной машины

1. Увеличиваем виртуальный диск средствами гипервизора на 1 ГБ
2. Увеличиваем PV (physical volume) командой
sudo pvresize /dev/sdb

3. Увеличиваем логический диск с одновременным расширением файловой системы

sudo lvextend -r -L+1G /dev/mapper/vg_test-vg_data, где
-r - расширение файловой системы
-L+1G - увеличение на 1ГБ
