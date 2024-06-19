--------------------------------------Videoprojekt von Gruppe 5-----------------------------------
https://github.com/johanneskrauss/videoprojekt
--------------------------------------------------------------------------------------------------
Ein Programm zum Einfügen eines Wasserzeichens in ein Bild, gesteuert über Eingaben in die Konsole. Es können sowohl Jpeg- als auch Png-Dateien bearbeitet werden. Auch Bilder mit
Alpha Kanal können eingelesen werden. 
Es kann sowohl ein Bild als auch ein Text als Wasserzeichen verwendet werden. Anschließend wird die Deckkraft sowie die Position des durch einen Mausklick in das Bild festgelegt.
Das fertige Bild mit Wasserzeichen kann anschließend gespeichert werden.
--------------------------------------------------------------------------------------------------
Genutzte Bibliotheken:
- OpenCV 4.10.0
- Numpy 1.26.4
- TkInter 8.6
Wichtige Hinweise:
- zum aktuellen Zeitpunkt (19.06.2024) läuft opencv nicht mit numpy 2.0, daher muss eine ältere Version von numpy installiert werden (hier 1.26.4)
- hierfür muss nach der Installation von opencv numpy zunächst deinstalliert werden und anschließend unter Angabe der gewünschten Version neu installiert werden.
- angelehnt an die Auflösungsspeicherung von Opencv sind Positionen und Auflösungen in y, x angegeben und nicht in x, y
