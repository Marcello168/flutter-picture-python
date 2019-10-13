<!--
 * @Author: gongyonghui
 * @Date: 2019-10-13 16:44:08
 * @LastEditors: gongyonghui
 * @LastEditTime: 2019-10-13 16:44:08
 * @Description: file content
 -->
# flutter-picture-python
Python 自动整理图片文件夹为 Flutter 资源图片文件夹

## Flutter 为当前设备加载适合其分辨率的图像
[`AssetImage`](https://docs.flutter.io/flutter/painting/AssetImage-class.html) 了解如何将逻辑请求asset映射到最接近当前设备像素比例的asset。为了使这种映射起作用，应该根据特定的目录结构来保存asset
* …/image.png
* …/Mx/image.png
* …/Nx/image.png
* …etc.
其中M和N是数字标识符，对应于其中包含的图像的分辨率，也就是说，它们指定不同素设备像比例的图片

主资源默认对应于1.0倍的分辨率图片。看一个例子：

* …/my_icon.png
* …/2.0x/my_icon.png
* …/3.0x/my_icon.png

在设备像素比率为1.8的设备上，`.../2.0x/my_icon.png` 将被选择。对于2.7的设备像素比率，`.../3.0x/my_icon.png`将被选择。

如果未在Image控件上指定渲染图像的宽度和高度，以便它将占用与主资源相同的屏幕空间量（并不是相同的物理像素），只是分辨率更高。 也就是说，如果`.../my_icon.png`是72px乘72px，那么`.../3.0x/my_icon.png`应该是216px乘216px; 但如果未指定宽度和高度，它们都将渲染为72像素×72像素（以逻辑像素为单位）。

`pubspec.yaml`中asset部分中的每一项都应与实际文件相对应，但主资源项除外。当主资源缺少某个资源时，会按分辨率从低到高的顺序去选择 （译者语：也就是说1x中没有的话会在2x中找，2x中还没有的话就在3x中找）。
#### 加载图片

要加载图片，请在widget的build方法中使用 [`AssetImage`](https://docs.flutter.io/flutter/painting/AssetImage-class.html)类。

例如，您的应用可以从上面的asset声明中加载背景图片：

```dart
Widget build(BuildContext context) {
  // ...
  return new DecoratedBox(
    decoration: new BoxDecoration(
      image: new DecorationImage(
        image: new AssetImage('graphics/background.png'),
        // ...
      ),
      // ...
    ),
  );
  // ...
}

```

使用默认的 asset bundle 加载资源时，内部会自动处理分辨率等，这些处理对开发者来说是无感知的。 (如果您使用一些更低级别的类，如 [`ImageStream`](https://docs.flutter.io/flutter/painting/ImageStream-class.html)或 [`ImageCache`](https://docs.flutter.io/flutter/painting/ImageCache-class.html), 您会注意到有与缩放相关的参数)

## 上面就是 Flutter 加载合适的分辨率的原理 但是 有时候 我们的UI给回来的切图 的文件夹结构 并不是 上面的那个样子 比如 


* …/Video/my_icon.png
* …/Video/my_icon@2x.png
* …/Video/my_icon@3x.png
* …/Video/my_icon1.png
* …/Video/my_icon1@2x.png
* …/Video/my_icon1@3x.png

那这个时候 我们需要把 图片 整理为 
* …/Video/my_icon.png
* …/Video/my_icon1.png
* …/Video/2.0x/my_icon.png
* …/Video/2.0x/my_icon1.png
* …/Video/3.0x/my_icon.png
* …/Video/3.0x/my_icon1.png

如果是手动一个一个改的话 非常麻烦 所以我用python 写了一个整理 成flutter 需要的图片文件夹 的脚本

## 使用方法 
  
  1. 下载 `picture.py` 文件
  2. 把该文件放到 图片文件夹的根目录下
  3.  执行 `python picture.py` 即可