from django.db import models


# Create your models here.
class Sanpham(models.Model):
    tensanpham = models.CharField("Tên sản phẩm", max_length=200)
    hinhanh = models.ImageField("Hình ảnh", upload_to="sanpham/")
    giatien = models.CharField("Giá tiền", max_length=50)
    noidung_gioithieu = models.TextField("Nội dung giới thiệu")
    ngaycapnhat = models.DateTimeField("Ngày cập nhật", auto_now=True)
    nguoicapnhat = models.CharField("Người cập nhật", max_length=200)

    def __str__(self):
        return self.tensanpham

class Baiviet(models.Model):
    tieude = models.CharField("Tiêu đề", max_length=200)
    noidung = models.TextField("Nội dung")
    nguoiviet = models.CharField("Người viết bài", max_length=50)
    danhmuc = models.CharField("Danh mục", max_length=200,
            default="None")
    ngayvietbai = models.DateTimeField("Ngày viết bài", auto_now_add=True)
    ngaycapnhat = models.DateTimeField("Ngày cập nhật", auto_now=True)

    def __str__(self):
        return self.tieude

class Danhmuc(models.Model):
    tendanhmuc = models.CharField("Tên danh mục", max_length=100)
    gioithieu = models.CharField("Giới thiệu", max_length=200)
    slug = models.CharField("Đường dẫn slug", max_length=200,
            default=1)
    class Meta:
        verbose_name_plural = "Danh mục"

    def __str__(self):
        return self.tendanhmuc
