import flet as ft


def main(page: ft.Page):
    page.title = "CeFah"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    vermelho = ft.colors.RED
    azul = ft.colors.BLUE

    teclado_numerico = ft.KeyboardType.NUMBER
    
    btn_estilo_celsius = ft.ButtonStyle(
        bgcolor=vermelho
    )
    btn_estilo_fahrenheit = ft.ButtonStyle(
        bgcolor=azul
    )

    def converter_celsius(e):
        try:
            c = int(caixa_celsius.value)
            f = (c * 9/5) + 32
            caixa_fahrenheit.value = int(f)
        except:
            caixa_celsius.value = ""
            caixa_fahrenheit.value = ""
        page.update()
        pass

    def converter_fahrenheit(e):
        try:
            f = int(caixa_fahrenheit.value)
            c = (f - 32) * 5/9
            caixa_celsius.value = int(c)
        except:
            caixa_celsius.value = ""
            caixa_fahrenheit.value = ""
        page.update()
        pass

    caixa_celsius = ft.TextField(label="Celsius", label_style=ft.TextStyle(color=vermelho), expand=True, keyboard_type=teclado_numerico, border_color=vermelho, color=vermelho)
    caixa_fahrenheit = ft.TextField(label="Fahrenheit", label_style=ft.TextStyle(color=azul), expand=True, keyboard_type=teclado_numerico, border_color=azul, color=azul)
    logo = ft.Image(src=f"CeFah/assets/icon.png", expand=True, expand_loose=True, width=200, height=200)
    btn_converter_celsius = ft.FilledButton(text="Celsius", expand=True, style=btn_estilo_celsius, on_click=converter_celsius)
    btn_converter_fahrenheit = ft.FilledButton(text="Fahrenheit", expand=True, style=btn_estilo_fahrenheit, on_click=converter_fahrenheit)

    page.add(logo)
    page.add(ft.Row([caixa_celsius, caixa_fahrenheit], ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([btn_converter_celsius, btn_converter_fahrenheit], ft.MainAxisAlignment.CENTER))
    page.update()


ft.app(main)
