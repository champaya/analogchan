import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .forms import ImageUploadForm
import cv2
import numpy as np


def home(request):
    # static/images/ ディレクトリ内の画像ファイル名を取得
    images_dir = os.path.join(settings.MEDIA_ROOT, 'images')  # MEDIA_ROOTを使用
    images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

    form = ImageUploadForm()
    context = {'images': images, 'form': form}
    return render(request, 'home.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)  # MEDIA_ROOTを使用

            # 画像ファイルの保存
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            return redirect('home')
    return HttpResponse("アップロードに失敗しました", status=400)

def delete_image(request, image_name):
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_name)  # MEDIA_ROOTを使用
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect('home')

def process_image(request):
    if request.method == 'POST':
        selected_image = request.POST.get('selected_image')
        resolution = request.POST.get('resolution')
        threshold_option = request.POST.get('threshold')

        # 表示する文字の取得
        char1 = request.POST.get('char1', '.')
        char2 = request.POST.get('char2', '+')
        char3 = request.POST.get('char3', '*')
        char4 = request.POST.get('char4', '0')

        # 画像処理関数を呼び出す
        output, one_line_count = image_processing(selected_image, resolution, threshold_option, char1, char2, char3, char4)

        # JSON形式で結果を返す
        return JsonResponse({'output': output, "one_line_count": one_line_count})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def image_processing(image_name, resolution, threshold_option, char1, char2, char3, char4):
    # 画像ファイルのパスを構築 (MEDIA_ROOT 内の images フォルダを参照)
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_name)

    # 画像を読み込む
    image = cv2.imread(image_path)

    # 画像が存在しない場合のエラーハンドリング
    if image is None:
        return "", 0

    # 解像度の設定
    if resolution == 'original':
        scale_factor = 1.0
    elif resolution == 'few':
        scale_factor = 0.75
    elif resolution == 'half':
        scale_factor = 0.5
    elif resolution == 'quarter':
        scale_factor = 0.25
    else: # octant
        scale_factor = 0.125

    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # BGRからRGBへ変換
    compressed_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # 画像のRGB配列を取得
    rgb_array = np.array(compressed_image_rgb)
    height, width, _ = rgb_array.shape

    display_array = np.zeros((height, width), dtype='<U1')

    # 閾値の設定
    if threshold_option == 'very_high':
        thresholds = [210, 170, 130]
    elif threshold_option == 'high':
        thresholds = [190, 150, 110]
    elif threshold_option == 'medium':
        thresholds = [170, 130, 90]
    elif threshold_option == 'low':
        thresholds = [150, 110, 70]
    else:  # very_low
        thresholds = [130, 90, 50]


    # 明るさの計算と分類
    for i in range(height):
        for j in range(width):
            R, G, B = rgb_array[i, j]
            dark_percentage = calculate_dark_percentage(R, G, B)
            if dark_percentage >= thresholds[0]:
                display_array[i, j] = char1
            elif dark_percentage >= thresholds[1]:
                display_array[i, j] = char2
            elif dark_percentage >= thresholds[2]:
                display_array[i, j] = char3
            else:
                display_array[i, j] = char4

    # 配列を文字列に変換
    output = '\n'.join([' '.join(row) for row in display_array])
    one_line_count = width
    return output, one_line_count


def calculate_dark_percentage(R, G, B):
    return 0.299 * R + 0.587 * G + 0.114 * B
