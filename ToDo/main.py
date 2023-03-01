import flet as ft

def main (page: ft.Page):


    def add_click(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()


    new_task = ft.TextField(hint_text="What's needs to be done? ", expand=True)

    tasks_view = ft.Column()
    
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_click),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)



ft.app(target=main)