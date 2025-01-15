import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Login Moderno"
    page.window_width = 450
    page.window_height = 600
    page.window_center()
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def login(e):
        if not email_input.value:
            email_input.error_text = "Por favor, digite seu email"
            page.update()
        elif not password_input.value:
            password_input.error_text = "Por favor, digite sua senha"
            page.update()
        else:
            print("Email:", email_input.value)
            print("Senha:", password_input.value)

    email_input = ft.TextField(
        label="Email",
        border_radius=8,
        text_size=14,
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_700,
        prefix_icon=ft.icons.EMAIL_OUTLINED,
    )

    password_input = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        border_radius=8,
        text_size=14,
        color=ft.colors.BLACK,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_700,
        prefix_icon=ft.icons.LOCK_OUTLINE,
    )

    login_button = ft.ElevatedButton(
        content=ft.Text(
            "Entrar",
            size=16,
            weight=ft.FontWeight.W_600,
        ),
        width=320,
        height=48,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
            shape={
                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=8),
            },
        ),
        on_click=login,
    )

    container = ft.Container(
        width=400,
        height=600,
        padding=30,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src="/api/placeholder/100/100",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text(
                    "Bem-vindo de volta!",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Faça login para continuar",
                    size=14,
                    color=ft.colors.GREY_700,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                email_input,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                password_input,
                ft.Container(
                    alignment=ft.alignment.center_right,
                    content=ft.TextButton(
                        "Esqueceu a senha?",
                        style=ft.ButtonStyle(
                            color=ft.colors.BLUE_700,
                        ),
                    ),
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                login_button,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "Não tem uma conta?",
                            size=14,
                            color=ft.colors.GREY_700,
                        ),
                        ft.TextButton(
                            "Registre-se",
                            style=ft.ButtonStyle(
                                color=ft.colors.BLUE_700,
                            ),
                        ),
                    ],
                ),
            ],
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                "#FFFFFF",
                "#F0F4FF",
            ],
        ),
    )

    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)