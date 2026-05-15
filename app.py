from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import os, random

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ---------- All Products (27 items) ----------
products = [
    # New Now (1-4)
    {
        'id': 1, 'name': 'Graphic T-Shirt', 'price': 1999,
        'image': '../static/images/Graphic T-Shirt1.jpg', 'sku': 'GTS-001',
        'design_details': 'Crew neck, short sleeves, graphic print, straight hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Jersey', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 2, 'name': 'Graphic T-Shirt', 'price': 1999,
        'image': '../static/images/Graphic T-Shirt2.jpg', 'sku': 'GTS-002',
        'design_details': 'Crew neck, short sleeves, graphic print, straight hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Jersey', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 3, 'name': 'Graphic T-Shirt', 'price': 1999,
        'image': '../static/images/Graphic T-Shirt3.jpg', 'sku': 'GTS-003',
        'design_details': 'Crew neck, short sleeves, graphic print, straight hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Jersey', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 4, 'name': 'Graphic T-Shirt', 'price': 1999,
        'image': '../static/images/Graphic T-Shirt4.jpg', 'sku': 'GTS-004',
        'design_details': 'Crew neck, short sleeves, graphic print, straight hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Jersey', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    # Summer Wear (5-8)
    {
        'id': 5, 'name': 'Oversized Summer Shirt', 'price': 1999,
        'image': '../static/images/SummerShirt1.jpg', 'sku': 'OSS-001',
        'design_details': 'Relaxed fit, short sleeves, drop shoulder, curved hem.',
        'style': 'Casual', 'fit': 'Oversized', 'fabric': 'Cotton', 'composition': '100% Cotton',
        'sizes': ['M', 'L', 'XL']
    },
    {
        'id': 6, 'name': 'Oversized Summer Shirt', 'price': 1999,
        'image': '../static/images/SummerShirt2.jpg', 'sku': 'OSS-002',
        'design_details': 'Relaxed fit, short sleeves, drop shoulder, curved hem.',
        'style': 'Casual', 'fit': 'Oversized', 'fabric': 'Cotton', 'composition': '100% Cotton',
        'sizes': ['M', 'L', 'XL']
    },
    {
        'id': 7, 'name': 'Oversized Summer Shirt', 'price': 1999,
        'image': '../static/images/SummerShirt3.jpg', 'sku': 'OSS-003',
        'design_details': 'Relaxed fit, short sleeves, drop shoulder, curved hem.',
        'style': 'Casual', 'fit': 'Oversized', 'fabric': 'Cotton', 'composition': '100% Cotton',
        'sizes': ['M', 'L', 'XL']
    },
    {
        'id': 8, 'name': 'Oversized Summer Shirt', 'price': 1999,
        'image': '../static/images/SummerShirt4.jpg', 'sku': 'OSS-004',
        'design_details': 'Relaxed fit, short sleeves, drop shoulder, curved hem.',
        'style': 'Casual', 'fit': 'Oversized', 'fabric': 'Cotton', 'composition': '100% Cotton',
        'sizes': ['M', 'L', 'XL']
    },
    # Winter Wear (9-12)
    {
        'id': 9, 'name': 'Flannel Shirt', 'price': 2200,
        'image': '../static/images/FlannelShirt1.jpg', 'sku': 'FS-001',
        'design_details': 'Long sleeves, button-up, chest pocket, curved hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Flannel', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 10, 'name': 'Flannel Shirt', 'price': 2200,
        'image': '../static/images/FlannelShirt2.jpg', 'sku': 'FS-002',
        'design_details': 'Long sleeves, button-up, chest pocket, curved hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Flannel', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 11, 'name': 'Flannel Shirt', 'price': 2200,
        'image': '../static/images/FlannelShirt3.jpg', 'sku': 'FS-003',
        'design_details': 'Long sleeves, button-up, chest pocket, curved hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Flannel', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    {
        'id': 12, 'name': 'Flannel Shirt', 'price': 2200,
        'image': '../static/images/FlannelShirt4.jpg', 'sku': 'FS-004',
        'design_details': 'Long sleeves, button-up, chest pocket, curved hem.',
        'style': 'Casual', 'fit': 'Regular', 'fabric': 'Flannel', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL']
    },
    # Sale (13-27)
    {
        'id': 13, 'name': 'Linen Casual Shirt – White', 'price': 1750, 'original_price': 2500,
        'image': '../static/images/Sale13.jpg', 'sku': 'SALE-013',
        'design_details': 'Lightweight linen, perfect for summer.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Linen', 'composition': '100% Linen',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 14, 'name': 'Cotton Linen Blend Short Sleeve Shirt', 'price': 2100, 'original_price': 3000,
        'image': '../static/images/Sale14.jpg', 'sku': 'SALE-014',
        'design_details': 'Breathable cotton-linen blend, short sleeves.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Cotton-Linen', 'composition': '60% Cotton, 40% Linen',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 15, 'name': 'Cotton Linen Blend Short Sleeve Shirt', 'price': 1750, 'original_price': 2500,
        'image': '../static/images/Sale15.jpg', 'sku': 'SALE-015',
        'design_details': 'Soft and comfortable for everyday wear.', 'style': 'Casual', 'fit': 'Relaxed', 'fabric': 'Cotton-Linen', 'composition': '60% Cotton, 40% Linen',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 16, 'name': 'Breathable Cotton Formal Shirt', 'price': 1400, 'original_price': 2000,
        'image': '../static/images/Sale16.jpg', 'sku': 'SALE-016',
        'design_details': 'Breathable cotton formal shirt with spread collar.', 'style': 'Formal', 'fit': 'Slim Fit', 'fabric': 'Cotton', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 17, 'name': 'Tropical Printed Cuban Collar Shirt', 'price': 2450, 'original_price': 3500,
        'image': '../static/images/Sale17.jpg', 'sku': 'SALE-017',
        'design_details': 'Vibrant tropical print, Cuban collar.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Viscose', 'composition': '100% Viscose',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 18, 'name': 'Wool Blend Formal Shirt', 'price': 1750, 'original_price': 2500,
        'image': '../static/images/Sale18.jpg', 'sku': 'SALE-018',
        'design_details': 'Wool blend for a polished look.', 'style': 'Formal', 'fit': 'Slim Fit', 'fabric': 'Wool Blend', 'composition': '50% Wool, 50% Polyester',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 19, 'name': 'Corduroy Button-Down Shirt', 'price': 2100, 'original_price': 3000,
        'image': '../static/images/Sale19.jpg', 'sku': 'SALE-019',
        'design_details': 'Classic corduroy with button-down collar.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Corduroy', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 20, 'name': 'Fleece-Lined Plaid Shirt', 'price': 1750, 'original_price': 2500,
        'image': '../static/images/Sale20.jpg', 'sku': 'SALE-020',
        'design_details': 'Warm fleece-lined plaid shirt.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Cotton/Polyester', 'composition': '80% Cotton, 20% Polyester',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 21, 'name': 'Classic Flannel Shirt – Red/Black Check', 'price': 1450, 'original_price': 2000,
        'image': '../static/images/Sale21.jpg', 'sku': 'SALE-021',
        'design_details': 'Timeless red and black check flannel.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Flannel', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 22, 'name': 'Plain Oxford Formal Shirt', 'price': 1450, 'original_price': 2000,
        'image': '../static/images/Sale22.jpg', 'sku': 'SALE-022',
        'design_details': 'Crisp Oxford fabric, button-down collar.', 'style': 'Formal', 'fit': 'Regular', 'fabric': 'Oxford', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 23, 'name': 'Denim Casual Shirt', 'price': 1750, 'original_price': 2500,
        'image': '../static/images/Sale23.jpg', 'sku': 'SALE-023',
        'design_details': 'Classic denim shirt, versatile and durable.', 'style': 'Casual', 'fit': 'Regular', 'fabric': 'Denim', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 24, 'name': 'Hawaiian Vacation Shirt', 'price': 2100, 'original_price': 3000,
        'image': '../static/images/Sale24.jpg', 'sku': 'SALE-024',
        'design_details': 'Fun Hawaiian print, perfect for vacations.', 'style': 'Casual', 'fit': 'Relaxed', 'fabric': 'Rayon', 'composition': '100% Rayon',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 25, 'name': 'Knit Textured Shirt', 'price': 1450, 'original_price': 2000,
        'image': '../static/images/Sale25.jpg', 'sku': 'SALE-025',
        'design_details': 'Subtle knit texture, modern silhouette.', 'style': 'Casual', 'fit': 'Slim Fit', 'fabric': 'Knit Cotton', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 26, 'name': 'Minimalist Poplin Shirt', 'price': 2100, 'original_price': 3000,
        'image': '../static/images/Sale26.jpg', 'sku': 'SALE-026',
        'design_details': 'Smooth poplin with a minimalist design.', 'style': 'Formal', 'fit': 'Regular', 'fabric': 'Poplin', 'composition': '100% Cotton',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    },
    {
        'id': 27, 'name': 'Longline Linen Shirt', 'price': 2100, 'original_price': 3000,
        'image': '../static/images/Sale27.jpg', 'sku': 'SALE-027',
        'design_details': 'Trendy longline cut in breathable linen.', 'style': 'Casual', 'fit': 'Oversized', 'fabric': 'Linen', 'composition': '100% Linen',
        'sizes': ['S', 'M', 'L', 'XL'], 'is_sale': True
    }
]

# ---------- Dummy Users ----------
users = [
    {'name': 'Test User', 'email': 'test@saifis.com', 'password': 'password123'}
]

# ---------- Cart Helper ----------
def get_cart_count():
    cart = session.get('cart', [])
    return sum(item['quantity'] for item in cart)

# ---------- Routes ----------
@app.route('/')
def index():
    return render_template('index.html', cart_count=get_cart_count(), products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    
    other_products = [p for p in products if p['id'] != product_id]
    suggested = random.sample(other_products, min(4, len(other_products)))
    
    return render_template('product.html', product=product, suggested_products=suggested, cart_count=get_cart_count())

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    item = request.json
    cart = session.get('cart', [])
    existing = None
    for ci in cart:
        if ci['id'] == item['id'] and ci.get('size') == item.get('size'):
            existing = ci
            break
    if existing:
        existing['quantity'] += item.get('quantity', 1)
    else:
        cart.append({
            'id': item['id'],
            'name': item['name'],
            'price': item['price'],
            'image': item.get('image', ''),
            'sku': item.get('sku', ''),
            'size': item.get('size', 'M'),
            'quantity': item.get('quantity', 1)
        })
    session['cart'] = cart
    return jsonify({'success': True, 'cart_count': get_cart_count()})

@app.route('/update-cart', methods=['POST'])
def update_cart():
    data = request.json
    cart_id = data.get('id')
    new_qty = data.get('quantity')
    size = data.get('size')
    cart = session.get('cart', [])
    for i, item in enumerate(cart):
        if item['id'] == cart_id and item.get('size') == size:
            if new_qty <= 0:
                cart.pop(i)
            else:
                cart[i]['quantity'] = new_qty
            break
    session['cart'] = cart
    return jsonify({'success': True, 'cart_count': get_cart_count()})

@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.json
    cart_id = data.get('id')
    size = data.get('size')
    cart = session.get('cart', [])
    cart = [item for item in cart if not (item['id'] == cart_id and item.get('size') == size)]
    session['cart'] = cart
    return jsonify({'success': True, 'cart_count': get_cart_count()})

@app.route('/cart')
def cart_page():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, cart_count=len(cart), total=total)

@app.route('/get-cart-count')
def cart_count():
    return jsonify({'cart_count': get_cart_count()})

@app.route('/search')
def search():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return render_template('search_results.html', query='', results=[], cart_count=get_cart_count())
    results = [p for p in products if query in p['name'].lower() or query in p['sku'].lower()]
    return render_template('search_results.html', query=query, results=results, cart_count=get_cart_count())

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = next((u for u in users if u['email'] == email and u['password'] == password), None)
        if user:
            session['user'] = {'name': user['name'], 'email': user['email']}
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('signin.html', cart_count=get_cart_count())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if any(u['email'] == email for u in users):
            flash('Email already registered. Please sign in.', 'error')
            return redirect(url_for('signin'))
        users.append({'name': name, 'email': email, 'password': password})
        session['user'] = {'name': name, 'email': email}
        flash('Account created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', cart_count=get_cart_count())

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/sale')
def sale():
    sale_products = [p for p in products if p.get('is_sale')]
    return render_template('sale.html', sale_products=sale_products, cart_count=get_cart_count())

@app.route('/shop-all')
def shop_all():
    return render_template('shop_all.html', products=products, cart_count=get_cart_count())

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    if not cart:
        return redirect(url_for('cart_page'))
    total = sum(item['price'] * item['quantity'] for item in cart)
    if request.method == 'POST':
        shipping = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'address': request.form.get('address'),
            'city': request.form.get('city'),
            'phone': request.form.get('phone')
        }
        order = {
            'shipping': shipping,
            'items': cart.copy(),
            'total': total,
            'order_id': 'ORD-' + str(int(os.urandom(4).hex(), 16))[-8:]
        }
        session['order'] = order
        session.pop('cart', None)
        return redirect(url_for('order_success'))
    return render_template('checkout.html', cart=cart, total=total, cart_count=get_cart_count())

@app.route('/order-success')
def order_success():
    order = session.get('order', None)
    if not order:
        return redirect(url_for('index'))
    return render_template('order_success.html', order=order, cart_count=get_cart_count())

if __name__ == '__main__':
    app.run(debug=True, port=5000)