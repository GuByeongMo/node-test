from flask import Flask, render_template, request

app = Flask(__name__)

# 핸드폰 데이터베이스
phones = [
    {'name': 'iPhone 13', 'brand': 'Apple', 'price': 1500000, 'type': 'iPhone'},
    {'name': 'Galaxy S22', 'brand': 'Samsung', 'price': 1300000, 'type': 'Galaxy S'},
    {'name': 'Galaxy Z Flip3', 'brand': 'Samsung', 'price': 2000000, 'type': 'Galaxy Z Flip'},
    # 추가적인 핸드폰 정보를 추가할 수 있습니다.
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    is_apple = request.form['is_apple']
    is_galaxy = request.form['is_galaxy']
    model = request.form['model']

    if is_apple == 'yes':

    else:
        if is_galaxy == 'yes':
            if model == 's':
                answer_text = "갤럭시 S의 가격은 50만원 이상입니다."
                recommendation = get_recommendation('Samsung', True, 'Galaxy S')
            elif model == 'z':
                answer_text = "갤럭시 Z FLIP의 가격은 50만원 이상입니다."
                recommendation = get_recommendation('Samsung', True, 'Galaxy Z Flip')
            else:
                answer_text = "잘못된 기종을 선택하셨습니다."
                recommendation = ""
        else:
            answer_text = "Apple 또는 갤럭시 휴대폰이 아닙니다."
            recommendation = ""

    return render_template('answer.html', answer_text=answer_text, recommendation=recommendation)

@app.route('/answer/yes', methods=['POST'])
def answer():
    price = request.form['price']
    is_galaxy = request.form['is_galaxy']
    model = request.form['model']

    if price == 'yes':
        answer_text = "Apple 휴대폰의 가격은 50만원 이상입니다."
        recommendation = get_recommendation('Apple', True)
    else:
        answer_text = "Apple 휴대폰의 가격은 50만원 미만입니다."
        recommendation = get_recommendation('Apple', False)
    if is_galaxy == 'yes':
        if model == 's':
               answer_text = "갤럭시 S의 가격은 50만원 이상입니다."
            recommendation = get_recommendation('Samsung', True, 'Galaxy S')
        elif model == 'z':
            answer_text = "갤럭시 Z FLIP의 가격은 50만원 이상입니다."
            recommendation = get_recommendation('Samsung', True, 'Galaxy Z Flip')
        else:
            answer_text = "잘못된 기종을 선택하셨습니다."
            recommendation = ""
    else:
        answer_text = "Apple 또는 갤럭시 휴대폰이 아닙니다."
        recommendation = ""
        
    return render_template('answer.html', answer_text=answer_text, recommendation=recommendation)

def get_recommendation(brand, is_expensive, phone_type=None):
    recommended_phones = []

    for phone in phones:
        if phone['brand'] == brand:
            if not phone_type or phone['type'] == phone_type:
                if is_expensive:
                    if phone['price'] >= 500000:
                        recommended_phones.append(phone)
                else:
                    if phone['price'] < 500000:
                        recommended_phones.append(phone)

    return recommended_phones

if __name__ == '__main__':
    app.run()