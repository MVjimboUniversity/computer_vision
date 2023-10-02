# Лабораторная работа № 1

Чтобы определить сигнала светофора, необходимо найти характерные пиксели для каждого из его цветов. Для этого изображения были представлены в цветовой модели HSV, и был произведен их первичный анализ.

В результате получили, что насыщенность (Saturation) и яркость (Value), соответствующие пикселям горящего сигнала светофора, имеют высокие значения. Поэтому, чтобы отделить эти пиксели, используются фильтры на насыщеннсоть и яркость. Чтобы определить цвет сигнала светофора использовались значения светового тона (Hue).

Также отдельно стоит отметить проблему того, что красный сигнал зачастую также мог восприниматься как желтый, так некоторые пиксели были слишком яркими и близкими к желтому цветовому тону. Чтобы избавиться от этой проблемы, в условие на наличие желтых пикселей было добавлена верхняя граница на яркость пикселей.