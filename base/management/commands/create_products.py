import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from base.models import Product, ProductFeatures

class Command(BaseCommand):
    help = 'Creates 70 clothing products with random data'

    def handle(self, *args, **kwargs):

        # Random clothing titles in Persian and English
        clothing_titles = [
            # T-Shirts
            "تیشرت مردانه نخی", "Men's Cotton T-Shirt", "تیشرت طرح دار", "Graphic T-Shirt",
            "تیشرت اسپرت", "Sport T-Shirt", "تیشرت آستین کوتاه", "Short Sleeve T-Shirt",
            
            # Shirts
            "پیراهن مردانه", "Men's Dress Shirt", "پیراهن رسمی", "Formal Shirt",
            "پیراهن کتان", "Linen Shirt", "پیراهن طرح دار", "Patterned Shirt",
            
            # Pants
            "شلوار جین", "Denim Jeans", "شلوار کتان", "Cotton Pants",
            "شلوار اسپرت", "Sport Pants", "شلوار رسمی", "Formal Pants",
            
            # Hoodies & Sweaters
            "هودی مردانه", "Men's Hoodie", "هودی زنانه", "Women's Hoodie",
            "پلیور پشمی", "Wool Sweater", "پلیور نخی", "Cotton Sweater",
            
            # Jackets & Coats
            "ژاکت زمستانی", "Winter Jacket", "کت چرمی", "Leather Jacket",
            "بارانی مردانه", "Men's Raincoat", "پافر", "Puffer Jacket",
            
            # Shorts
            "شلوارک مردانه", "Men's Shorts", "شلوارک اسپرت", "Sport Shorts",
            
            # Other
            "بلوز زنانه", "Women's Blouse", "تاپ ورزشی", "Sport Top",
            "لباس راحتی", "Casual Wear", "لباس مجلسی", "Party Wear"
        ]

        # Random product descriptions
        descriptions = [
            "محصولی با کیفیت عالی و دوام بالا. مناسب برای استفاده روزمره",
            "High quality product with excellent durability. Perfect for daily use",
            "ساخته شده از بهترین مواد اولیه. راحت و با طراحی شیک",
            "Made from the finest materials. Comfortable and stylish design",
            "مناسب برای تمام فصول. قابل شستشو و نگهداری آسان",
            "Suitable for all seasons. Easy to wash and maintain",
            "طراحی مدرن و امروزی. با توجه به آخرین مدل های روز",
            "Modern and contemporary design. Following the latest fashion trends",
            "محصولی سبک و راحت. ایده آل برای مسافرت و ورزش",
            "Lightweight and comfortable. Ideal for travel and sports"
        ]

        # Random product features
        feature_titles = [
            "نخی", "Cotton", "پنبه ای", "کتان", "Linen", "پشمی", "Wool",
            "الاستیک", "Stretch", "ضد حساسیت", "Hypoallergenic", "تنفس پذیر", "Breathable",
            "ضد چروک", "Anti-wrinkle", "ضد آب", "Water resistant", "سایز استاندارد", "Standard fit",
            "گرم", "Warm", "خنک", "Cool", "سبک", "Lightweight", "با دوام", "Durable",
            "قابل شستشو با ماشین", "Machine washable", "رنگ ثابت", "Color fast"
        ]

        # First, create some product features if they don't exist
        self.stdout.write("Creating product features...")
        features = []
        for feature_title in feature_titles:
            feature, created = ProductFeatures.objects.get_or_create(title=feature_title)
            features.append(feature)
            if created:
                self.stdout.write(f"Created feature: {feature_title}")

        # Create 70 products
        self.stdout.write("Creating 70 clothing products...")
        
        for i in range(70):
            # Random data generation
            title = random.choice(clothing_titles)
            price = 10 * random.randint(2, 50)  # Random price between 50,000 and 500,000
            discount = random.choice([0, 0, 0, 0, 10, 15, 20, 25, 30])  # Mostly no discount, sometimes 10-30%
            size = random.choice(['0', '1', '2', '3'])  # Random size
            is_active = True  
            
            # Create the product
            product = Product.objects.create(
                title=f"{title} مدل {i+1}",
                details=random.choice(descriptions),
                price=price,
                size=size,
                discount=discount,
                is_active=is_active
            )
            
            # Add random features to the product (2-5 random features)
            num_features = random.randint(2, 5)
            product_features = random.sample(features, num_features)
            product.productFeatures.set(product_features)
            
            self.stdout.write(f"Created product: {product.title} - Price: {price} - Discount: {discount}% - Size: {product.get_size_display()}")

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created 70 clothing products with random data!'
            )
        )