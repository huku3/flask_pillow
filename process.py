from PIL import Image
#Image.openで画像を開く
img = Image.open("images/cat.png")
frame = Image.open("images/frame.png")
#変数にフレームの画像のリサイズは、resize()メソッドで、引数にタプル型で
#(幅、高さ)を指定することで行うことができます。
resized_frame = frame.resize((img.width, img.height))

#画像の合成
img.paste(resized_frame, (0, 0), resized_frame)
#合成した画像の保存　out.pngと命名
img.save("images/out.png")

img.show()

# img.show() 画像の表示
#※show()メソッドは、指定したimgを直接開いているわけではなく
#一時的なtempファイルが作成されそのファイルを開いています。
#そのため、ファイル名がtmpXXXXとなっています。
