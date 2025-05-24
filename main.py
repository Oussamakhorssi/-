import flet as ft
from flet import (
    Page,
    AppBar,
    Text,
    Icon,
    TextField,
    Row,
    Column,
    Container,
    Card,
    ElevatedButton,
    Image,
    IconButton,
    ListView,
    Divider,
    alignment,
    border_radius,
    padding,
    margin,
    animation,
    CircleAvatar,
    BoxShadow,
    LinearGradient,
    Alignment,
    ScrollMode,
    Stack,
    GestureDetector
)
# Devloped By Fares Benatmane

#  colors
PRIMARY_COLOR = "#347175"
ACCENT_COLOR = "#FFFFFF"
CONTRAST_COLOR = "#7aa1a2"
TEXT_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#dee6e6"
CARD_COLOR = "#FFFFFF"
SHADOW_COLOR = "#00000029"
SECONDARY_COLOR = "#7aa1a2"
TERTIARY_COLOR = "#347175"

class MedicineApp:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "علاجي - تطبيق طبي"
        self.page.padding = 0
        self.page.bgcolor = BACKGROUND_COLOR
        self.page.theme = ft.Theme(color_scheme_seed=PRIMARY_COLOR)
        self.page.rtl = True
        self.page.scroll = ScrollMode.AUTO
        self.page.window_width = 400
        self.page.window_min_width = 350
        self.page.window_max_width = 500


        self.current_view = "splash"

        # (ar = Arabic, fr = French)
        self.current_language = "ar"


        self.translations = {
            "ar": {
                "app_title": "علاجي",
                "app_subtitle": "تطبيق طبي",
                "choose_service": "اختر الخدمة",
                "medicine_search": "البحث عن دواء",
                "doctor_search": "البحث عن طبيب",
                "ai_chat": "التحدث مع الذكاء الاصطناعي",
                "other_services": "خدمات أخرى",
                "back": "العودة",
                "search_medicine": "ابحث عن دواء...",
                "search_doctor": "ابحث عن طبيب...",
                "nearby_pharmacies": "الصيدليات القريبة",
                "view_all": "عرض الكل",
                "distance": "المسافة",
                "open": "مفتوح",
                "closed": "مغلق",
                "directions": "الاتجاهات",
                "pharmacies_near_you": "صيدليات قريبة منك",
                "find_medicines_easily": "اعثر على الأدوية بسهولة",
            },
            "fr": {
                "app_title": "Alaji",
                "app_subtitle": "Application Médicale",
                "choose_service": "Choisir un Service",
                "medicine_search": "Rechercher un Médicament",
                "doctor_search": "Rechercher un Médecin",
                "ai_chat": "Discuter avec l'IA",
                "other_services": "Autres Services",
                "back": "Retour",
                "search_medicine": "Rechercher un médicament...",
                "search_doctor": "Rechercher un médecin...",
                "nearby_pharmacies": "Pharmacies à Proximité",
                "view_all": "Voir Tout",
                "distance": "Distance",
                "open": "Ouvert",
                "closed": "Fermé",
                "directions": "Directions",
                "pharmacies_near_you": "Pharmacies près de chez vous",
                "find_medicines_easily": "Trouvez des médicaments facilement",
            }
        }


        self.setup_app_bar()
        self.setup_content()


        self.page.add(
            self.app_bar,
            self.content
        )


        self.show_splash_screen()

    def setup_app_bar(self):

        custom_title = Text(
            self.translations[self.current_language]["app_title"],
            color=TEXT_COLOR,
            size=30,
            font_family="ThuluthFont",
            weight="bold",
            text_align="center",
        )


        lang_tooltip = "Changer la langue" if self.current_language == "ar" else "تغيير اللغة"

        self.app_bar = AppBar(
            title=custom_title,
            bgcolor=PRIMARY_COLOR,
            center_title=True,
            elevation=4,
            leading=IconButton(
                icon=ft.icons.MEDICATION_LIQUID,
                icon_color=ACCENT_COLOR,
                tooltip=self.translations[self.current_language]["back"],
                on_click=self.go_to_home
            ),
            actions=[
                IconButton(
                    icon=ft.icons.LANGUAGE_SHARP,
                    icon_color=TEXT_COLOR,
                    tooltip=lang_tooltip,
                    on_click=self.toggle_language
                )
            ],
        )

    def toggle_language(self, e):
        """Toggle between Arabic and French languages"""

        self.current_language = "fr" if self.current_language == "ar" else "ar"


        self.page.rtl = self.current_language == "ar"


        self.setup_app_bar()


        if self.current_view == "splash":
            self.show_splash_screen()
        elif self.current_view == "medicine_search":
            self.content.content = self.build_medicine_search_view()
            self.content.update()
        elif self.current_view == "doctor_search":
            self.content.content = self.build_doctor_search_view()
            self.content.update()
        elif self.current_view == "ai_chat":
            self.content.content = self.build_ai_chat_view()
            self.content.update()
        elif self.current_view == "other_services":
            self.content.content = self.build_other_services_view()
            self.content.update()


        self.page.update()

    def setup_content(self):
        # Container for the main
        self.content = Container(
            expand=True,
            content=None
        )

    def show_splash_screen(self):
        """Show the splash screen with logo and service buttons"""
        self.current_view = "splash"

        # service buttons
        medicine_search_btn = self.create_service_button(
            self.translations[self.current_language]["medicine_search"],
            ft.icons.MEDICATION,
            ACCENT_COLOR,
            self.show_medicine_search
        )

        doctor_search_btn = self.create_service_button(
            self.translations[self.current_language]["doctor_search"],
            ft.icons.MEDICAL_SERVICES,
            SECONDARY_COLOR,
            self.show_doctor_search
        )


        ai_chat_btn = Container(
            content=ElevatedButton(
                content=Row(
                    controls=[
                        Container(
                            content=Icon(ft.icons.SMART_TOY, color=TEXT_COLOR, size=24),
                            width=24,
                            height=24,
                        ),
                        Text(self.translations[self.current_language]["ai_chat"], size=16, weight="bold"),
                    ],
                    alignment="center",
                    spacing=10,
                ),
                style=ft.ButtonStyle(
                    color={"": TEXT_COLOR},
                    bgcolor={"": TERTIARY_COLOR},
                    padding=padding.all(20),
                    shape=ft.RoundedRectangleBorder(radius=10),
                    shadow_color=SHADOW_COLOR,
                    elevation={"": 5, "hovered": 10},
                ),
                width=300,
                on_click=self.show_ai_chat,
            ),
            animate=animation.Animation(300, "decelerate"),
        )

        other_services_btn = self.create_service_button(
            self.translations[self.current_language]["other_services"],
            ft.icons.MISCELLANEOUS_SERVICES,
            CONTRAST_COLOR,
            self.show_other_services
        )


        logo_container = Container(
            content=Stack([

                Container(
                    width=160,
                    height=160,
                    border_radius=border_radius.all(100),
                    gradient=LinearGradient(
                        begin=Alignment(0, 0),
                        end=Alignment(1, 1),
                        colors=[
                            PRIMARY_COLOR,
                            CONTRAST_COLOR,
                        ],
                    ),
                    alignment=alignment.center,
                ),

                Container(
                    width=140,
                    height=140,
                    border_radius=border_radius.all(90),
                    bgcolor=BACKGROUND_COLOR,
                    alignment=alignment.center,
                    content=Image(
                        src="assets/logo.png",
                        width=120,
                        height=120,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                ),

                Container(
                    width=160,
                    height=160,
                    alignment=alignment.center,
                    content=Text(
                        "علاجي",
                        size=45,
                        weight="bold",
                        color=PRIMARY_COLOR,
                        font_family="ThuluthFont",
                    ),
                    offset=ft.transform.Offset(0, 40),
                ),
            ]),
            alignment=alignment.center,
            animate=animation.Animation(1000, "bounceOut"),
            margin=margin.only(bottom=20),
        )


        splash_content = Container(
            content=Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=30,
                controls=[
                    Container(height=40),
                    logo_container,
                    Container(
                        content=Text(
                            self.translations[self.current_language]["choose_service"],
                            size=28,
                            weight="bold",
                            color=PRIMARY_COLOR,
                        ),
                        margin=margin.only(top=20, bottom=10),
                    ),
                    Container(
                        content=Column(
                            spacing=15,
                            horizontal_alignment="center",
                            controls=[
                                medicine_search_btn,
                                doctor_search_btn,
                                ai_chat_btn,
                                other_services_btn,
                            ],
                        ),
                        width=320,
                    ),
                ],
            ),
            padding=padding.all(20),
            width=self.page.width,
            height=self.page.height,
        )

        self.content.content = splash_content
        self.content.update()

    def create_service_button(self, text, icon, color, on_click_handler):
        """Create a styled service button"""
        return Container(
            content=ElevatedButton(
                content=Row(
                    controls=[
                        Icon(icon, color=TEXT_COLOR, size=24),
                        Text(text, size=16, weight="bold"),
                    ],
                    alignment="center",
                    spacing=10,
                ),
                style=ft.ButtonStyle(
                    color={"": TEXT_COLOR},
                    bgcolor={"": color},
                    padding=padding.all(20),
                    shape=ft.RoundedRectangleBorder(radius=10),
                    shadow_color=SHADOW_COLOR,
                    elevation={"": 5, "hovered": 10},
                ),
                width=300,
                on_click=on_click_handler,
            ),
            animate=animation.Animation(300, "decelerate"),
        )

    def go_to_home(self, e=None):
        """Return to home/splash screen"""
        self.show_splash_screen()

    def show_medicine_search(self, e):
        """Show medicine search view"""
        self.current_view = "medicine_search"
        self.content.content = self.build_medicine_search_view()
        self.content.update()

    def show_doctor_search(self, e):
        """Show doctor search view"""
        self.current_view = "doctor_search"
        self.content.content = self.build_doctor_search_view()
        self.content.update()

    def show_ai_chat(self, e):
        """Show AI chat view"""
        self.current_view = "ai_chat"
        self.content.content = self.build_ai_chat_view()
        self.content.update()

    def show_other_services(self, e):
        """Show other services view"""
        self.current_view = "other_services"
        self.content.content = self.build_other_services_view()
        self.content.update()

    def build_medicine_search_view(self):
        """Build the medicine search view"""

        back_button = IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=PRIMARY_COLOR,
            tooltip=self.translations[self.current_language]["back"],
            on_click=self.go_to_home
        )

        # Searchb
        search_row = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                # Search field
                Container(
                    content=TextField(
                        color='#6fc5c7',
                        hint_text=self.translations[self.current_language]["search_medicine"],
                        prefix_icon=ft.icons.MEDICATION,
                        border_radius=border_radius.all(20),
                        bgcolor=CARD_COLOR,
                        border_color=PRIMARY_COLOR,
                        content_padding=padding.only(left=20, right=20, top=10, bottom=10),
                        width=self.page.width * 0.75,
                        focused_border_color=ACCENT_COLOR,
                        focused_border_width=2,
                    ),
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=8,
                        color=SHADOW_COLOR,
                        offset=ft.Offset(0, 2),
                    ),
                    animate=animation.Animation(300, "decelerate"),
                ),


                Container(
                    content=ElevatedButton(
                        content=Text(
                            "AI",
                            size=16,
                            weight="bold",
                            color=TEXT_COLOR,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor={"": TERTIARY_COLOR},
                            shape=ft.CircleBorder(),
                            padding=padding.all(12),
                        ),
                        on_click=self.show_ai_chat,
                    ),
                    tooltip=self.translations[self.current_language]["ai_chat"],
                    animate=animation.Animation(300, "decelerate"),
                ),
            ],
            width=self.page.width * 0.9,
        )


        search_container = Container(
            content=search_row,
            margin=margin.only(bottom=15, top=5),
        )


        pharmacy_image = Container(
            content=Stack([

                Image(
                    src="assets/pharma.jpg",
                    width=self.page.width * 0.9,
                    height=200,
                    fit=ft.ImageFit.COVER,
                    border_radius=border_radius.all(15),
                ),
                # Overlay gradient
                Container(
                    gradient=LinearGradient(
                        begin=Alignment(-0.2, 1.0),
                        end=Alignment(0.2, 0.0),
                        colors=[
                            ft.colors.with_opacity(0.8, PRIMARY_COLOR),
                            ft.colors.with_opacity(0.0, PRIMARY_COLOR),
                        ],
                    ),
                    border_radius=border_radius.all(15),
                    height=200,
                    width=self.page.width * 0.9,
                ),
                # overlay
                Container(
                    content=Column(
                        controls=[
                            Text(
                                self.translations[self.current_language]["pharmacies_near_you"],
                                color='#347175',
                                size=20,
                                weight="bold",
                            ),
                            Text(
                                self.translations[self.current_language]["find_medicines_easily"],
                                color='#347175',
                                size=14,
                                weight="w400",
                            ),
                        ],
                        spacing=5,
                        horizontal_alignment="center",
                    ),
                    padding=padding.only(bottom=20),
                    alignment=alignment.bottom_center,
                    width=self.page.width * 0.9,
                ),
            ]),
            border_radius=border_radius.all(15),
            margin=margin.only(top=10, bottom=20),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=SHADOW_COLOR,
                offset=ft.Offset(0, 3),
            ),
            animate=animation.Animation(500, "decelerate"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        )

        # Section title
        pharmacy_title = Row(
            alignment="spaceBetween",
            controls=[
                Row(
                    controls=[
                        Container(
                            width=4,
                            height=20,
                            bgcolor=ACCENT_COLOR,
                            border_radius=border_radius.all(10),
                            margin=margin.only(right=8),
                        ),
                        Text(self.translations[self.current_language]["nearby_pharmacies"], size=18, weight="bold"),
                    ],
                ),
                Text(self.translations[self.current_language]["view_all"], size=14, color=CONTRAST_COLOR),
            ],
            width=self.page.width * 0.9,
        )

        # Nearby pharmacies
        pharmacy_list = ListView(
            spacing=10,
            padding=padding.all(0),
            height=220,
            width=self.page.width * 0.9,
        )


        if self.current_language == "ar":
            pharmacies = [
                {"name": "صيدلية الشفاء", "distance": "0.5 كم", "status": "مفتوح", "rating": "4.8"},
                {"name": "صيدلية الرحمة", "distance": "1.2 كم", "status": "مفتوح", "rating": "4.5"},
                {"name": "صيدلية الصحة", "distance": "2.0 كم", "status": "مغلق", "rating": "4.2"},
            ]
        else:
            pharmacies = [
                {"name": "Pharmacie Al-Shifa", "distance": "0.5 km", "status": "Ouvert", "rating": "4.8"},
                {"name": "Pharmacie Al-Rahma", "distance": "1.2 km", "status": "Ouvert", "rating": "4.5"},
                {"name": "Pharmacie Al-Saha", "distance": "2.0 km", "status": "Fermé", "rating": "4.2"},
            ]

        for pharmacy in pharmacies:
            pharmacy_card = Container(
                content=Card(
                    content=Container(
                        padding=padding.all(15),
                        content=Column(
                            spacing=10,
                            controls=[
                                Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Row(
                                            controls=[
                                                CircleAvatar(
                                                    content=Icon(
                                                        ft.icons.LOCAL_PHARMACY,
                                                        color=TEXT_COLOR,
                                                        size=18,
                                                    ),
                                                    bgcolor=PRIMARY_COLOR,
                                                    radius=16,
                                                ),
                                                Container(width=10),
                                                Column(
                                                    spacing=2,
                                                    controls=[
                                                        Text(pharmacy["name"], weight="bold"),
                                                        Text(f"{self.translations[self.current_language]['distance']}: {pharmacy['distance']}", size=12),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Container(
                                            padding=padding.symmetric(horizontal=8, vertical=4),
                                            bgcolor=ACCENT_COLOR if pharmacy["status"] == "مفتوح" else "#E53E3E",
                                            border_radius=border_radius.all(5),
                                            content=Text(pharmacy["status"], color=TEXT_COLOR, size=12),
                                        ),
                                    ],
                                ),
                                Divider(height=1, color="#E2E8F0"),
                                Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Row(
                                            controls=[
                                                Icon(ft.icons.STAR, color="#F6E05E", size=16),
                                                Text(pharmacy["rating"], size=14, weight="w500"),
                                            ],
                                            spacing=4,
                                        ),
                                        ElevatedButton(
                                            content=Row(
                                                controls=[
                                                    Icon(ft.icons.DIRECTIONS, size=14, color=TEXT_COLOR),
                                                    Text(self.translations[self.current_language]["directions"], size=12),
                                                ],
                                                spacing=4,
                                            ),
                                            style=ft.ButtonStyle(
                                                color={"": TEXT_COLOR},
                                                bgcolor={"": CONTRAST_COLOR},
                                                padding=padding.all(10),
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    elevation=2,
                ),
                margin=margin.only(bottom=5),
                animate=animation.Animation(200, "decelerate"),
            )
            pharmacy_list.controls.append(pharmacy_card)


        return Container(
            padding=padding.all(15),
            content=Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            back_button,
                            Text(self.translations[self.current_language]["medicine_search"], size=22, weight="bold"),
                            Container(width=48),
                        ],
                        width=self.page.width * 0.9,
                    ),
                    search_container,
                    pharmacy_image,
                    pharmacy_title,
                    pharmacy_list,
                ],
            ),
        )

    def build_doctor_search_view(self):
        """Build the doctor search view"""

        back_button = IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=PRIMARY_COLOR,
            tooltip=self.translations[self.current_language]["back"],
            on_click=self.go_to_home
        )


        search_row = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                # Search field
                Container(
                    content=TextField(
                        hint_text=self.translations[self.current_language]["search_doctor"],
                        color='#6fc5c7',
                        prefix_icon=ft.icons.PERSON_SEARCH,
                        border_radius=border_radius.all(20),
                        bgcolor=CARD_COLOR,
                        border_color=SECONDARY_COLOR,
                        content_padding=padding.only(left=20, right=20, top=10, bottom=10),
                        width=self.page.width * 0.75,
                        focused_border_color=SECONDARY_COLOR,
                        focused_border_width=2,
                    ),
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=8,
                        color=SHADOW_COLOR,
                        offset=ft.Offset(0, 2),
                    ),
                    animate=animation.Animation(300, "decelerate"),
                ),

                # AI button jdida
                Container(
                    content=ElevatedButton(
                        content=Text(
                            "AI",
                            size=16,
                            weight="bold",
                            color=TEXT_COLOR,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor={"": TERTIARY_COLOR},
                            shape=ft.CircleBorder(),
                            padding=padding.all(12),
                        ),
                        on_click=self.show_ai_chat,
                    ),
                    tooltip=self.translations[self.current_language]["ai_chat"],
                    animate=animation.Animation(300, "decelerate"),
                ),
            ],
            width=self.page.width * 0.9,
        )

        # Container for the search row
        search_container = Container(
            content=search_row,
            margin=margin.only(bottom=15, top=5),
        )

        # Filter options
        if self.current_language == "ar":
            filter_texts = [
                {"text": "الكل", "selected": True},
                {"text": "أطباء عامون", "selected": False},
                {"text": "أطباء أطفال", "selected": False},
                {"text": "أطباء نساء", "selected": False},
            ]
        else:
            filter_texts = [
                {"text": "Tous", "selected": True},
                {"text": "Médecins généralistes", "selected": False},
                {"text": "Pédiatres", "selected": False},
                {"text": "Gynécologues", "selected": False},
            ]

        filter_controls = []
        for filter_item in filter_texts:
            filter_controls.append(
                Container(
                    content=Text(
                        filter_item["text"],
                        color=TEXT_COLOR if filter_item["selected"] else PRIMARY_COLOR,
                        size=14,
                        weight="bold" if filter_item["selected"] else "normal"
                    ),
                    bgcolor=SECONDARY_COLOR if filter_item["selected"] else CARD_COLOR,
                    padding=padding.symmetric(horizontal=15, vertical=8),
                    border_radius=border_radius.all(20),
                )
            )

        filter_options = Row(
            spacing=10,
            scroll="auto",
            controls=filter_controls,
            width=self.page.width * 0.9,
        )

        # Doctors list
        doctors_list = ListView(
            spacing=15,
            padding=padding.all(0),
            height=400,
            width=self.page.width * 0.9,
        )

        # Add dummy doctors
        if self.current_language == "ar":
            doctors = [
                {
                    "name": "د. أحمد محمد",
                    "specialty": "طبيب عام",
                    "rating": "4.9",
                    "distance": "1.2 كم",
                    "available": True,
                    "available_text": "متاح اليوم",
                    "not_available_text": "غير متاح اليوم",
                    "book_appointment": "حجز موعد"
                },
                {
                    "name": "د. سارة علي",
                    "specialty": "طبيب أسنان",
                    "rating": "4.7",
                    "distance": "2.5 كم",
                    "available": True,
                    "available_text": "متاح اليوم",
                    "not_available_text": "غير متاح اليوم",
                    "book_appointment": "حجز موعد"
                },
                {
                    "name": "د. محمد خالد",
                    "specialty": "طبيب أطفال",
                    "rating": "4.8",
                    "distance": "3.0 كم",
                    "available": False,
                    "available_text": "متاح اليوم",
                    "not_available_text": "غير متاح اليوم",
                    "book_appointment": "حجز موعد"
                },
            ]
        else:
            doctors = [
                {
                    "name": "Dr. Ahmed Mohamed",
                    "specialty": "Médecin généraliste",
                    "rating": "4.9",
                    "distance": "1.2 km",
                    "available": True,
                    "available_text": "Disponible aujourd'hui",
                    "not_available_text": "Non disponible aujourd'hui",
                    "book_appointment": "Prendre RDV"
                },
                {
                    "name": "Dr. Sara Ali",
                    "specialty": "Dentiste",
                    "rating": "4.7",
                    "distance": "2.5 km",
                    "available": True,
                    "available_text": "Disponible aujourd'hui",
                    "not_available_text": "Non disponible aujourd'hui",
                    "book_appointment": "Prendre RDV"
                },
                {
                    "name": "Dr. Mohamed Khaled",
                    "specialty": "Pédiatre",
                    "rating": "4.8",
                    "distance": "3.0 km",
                    "available": False,
                    "available_text": "Disponible aujourd'hui",
                    "not_available_text": "Non disponible aujourd'hui",
                    "book_appointment": "Prendre RDV"
                },
            ]

        for doctor in doctors:
            doctor_card = Container(
                content=Card(
                    content=Container(
                        padding=padding.all(15),
                        content=Column(
                            spacing=10,
                            controls=[
                                Row(
                                    alignment="start",
                                    controls=[
                                        CircleAvatar(
                                            content=Text(
                                                doctor["name"][3:5],
                                                color=TEXT_COLOR,
                                                size=18,
                                                weight="bold",
                                            ),
                                            bgcolor=SECONDARY_COLOR,
                                            radius=25,
                                        ),
                                        Container(width=15),
                                        Column(
                                            spacing=2,
                                            controls=[
                                                Text(doctor["name"], weight="bold", size=16),
                                                Text(doctor["specialty"], size=14, color=CONTRAST_COLOR),
                                                Row(
                                                    controls=[
                                                        Icon(ft.icons.STAR, color="#F6E05E", size=14),
                                                        Text(doctor["rating"], size=12),
                                                        Container(width=10),
                                                        Icon(ft.icons.LOCATION_ON, color=CONTRAST_COLOR, size=14),
                                                        Text(doctor["distance"], size=12),
                                                    ],
                                                    spacing=2,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Divider(height=1, color="#E2E8F0"),
                                Row(
                                    alignment="spaceBetween",
                                    controls=[
                                        Container(
                                            content=Text(
                                                doctor["available_text"] if doctor["available"] else doctor["not_available_text"],
                                                color=TEXT_COLOR if doctor["available"] else "#E53E3E",
                                                size=12,
                                                weight="bold",
                                            ),
                                            bgcolor=ACCENT_COLOR if doctor["available"] else ft.colors.with_opacity(0.1, "#E53E3E"),
                                            padding=padding.symmetric(horizontal=10, vertical=5),
                                            border_radius=border_radius.all(5),
                                        ),
                                        ElevatedButton(
                                            content=Text(doctor["book_appointment"], size=14),
                                            style=ft.ButtonStyle(
                                                color={"": TEXT_COLOR},
                                                bgcolor={"": SECONDARY_COLOR},
                                                padding=padding.symmetric(horizontal=15, vertical=10),
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                            ),
                                            disabled=not doctor["available"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    elevation=2,
                ),
                animate=animation.Animation(200, "decelerate"),
            )
            doctors_list.controls.append(doctor_card)


        return Container(
            padding=padding.all(15),
            content=Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            back_button,
                            Text(self.translations[self.current_language]["doctor_search"], size=22, weight="bold"),
                            Container(width=48),
                        ],
                        width=self.page.width * 0.9,
                    ),
                    search_container,
                    filter_options,
                    Container(height=10),
                    doctors_list,
                ],
            ),
        )

    def build_ai_chat_view(self):
        """Build the AI chat view"""

        back_button = IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=PRIMARY_COLOR,
            tooltip=self.translations[self.current_language]["back"],
            on_click=self.go_to_home
        )

        # Chat messages
        chat_messages = ListView(
            spacing=10,
            padding=padding.all(10),
            height=400,
            width=self.page.width * 0.9,
        )

        # FARES BENATMANE



        ai_message = Container(
            content=Row(
                controls=[
                    CircleAvatar(
                        content=Icon(ft.icons.SMART_TOY, color=TEXT_COLOR, size=16),
                        bgcolor=TERTIARY_COLOR,
                        radius=16,
                    ),
                    Container(
                        content=Column(
                            controls=[
                                Text(
                                    "Assistant Médical" if self.current_language == "fr" else "المساعد الطبي",
                                    size=12,
                                    color=CONTRAST_COLOR
                                ),
                                Container(
                                    content=Text(
                                        "Bienvenue dans l'assistant médical intelligent. Comment puis-je vous aider aujourd'hui?" if self.current_language == "fr" else "مرحباً بك في المساعد الطبي الذكي. كيف يمكنني مساعدتك اليوم؟",
                                        size=14, color='#6fc5c7'
                                    ),
                                    bgcolor=CARD_COLOR,
                                    border_radius=border_radius.only(
                                        top_right=10, bottom_left=10, bottom_right=10
                                    ),
                                    padding=padding.all(10),
                                    width=self.page.width * 0.7,
                                ),
                            ],
                            spacing=5,
                            width=self.page.width * 0.75,
                        ),
                        margin=margin.only(left=10),
                    ),
                ],
                alignment="start",
            ),
            margin=margin.only(bottom=10),
        )

        chat_messages.controls.append(ai_message)

        # Suggestions
        if self.current_language == "ar":
            suggestion_texts = [
                "اقترح طبيب مناسب",
                "كيف أخفض الحرارة؟",
                "من يوفر هذا الدواء"
            ]
        else:
            suggestion_texts = [
                "Suggérer un médecin",
                "Comment réduire la fièvre?",
                "Qui fournit ce médicament"
            ]

        suggestion_controls = []
        for text in suggestion_texts:
            suggestion_controls.append(
                Container(
                    content=Text(text, size=12, color='#6fc5c7'),
                    bgcolor=CARD_COLOR,
                    padding=padding.symmetric(horizontal=15, vertical=8),
                    border_radius=border_radius.all(20),
                    border=ft.border.all(1, TERTIARY_COLOR),
                )
            )

        suggestions = Row(
            spacing=10,
            scroll="auto",
            controls=suggestion_controls,
            width=self.page.width * 0.9,
        )


        chat_input = Container(
            content=Row(
                controls=[
                    TextField(
                        hint_text="Écrivez votre question ici..." if self.current_language == "fr" else "اكتب سؤالك هنا...",
                        color='#6fc5c7',
                        border_radius=border_radius.all(20),
                        bgcolor=CARD_COLOR,
                        border_color=TERTIARY_COLOR,
                        content_padding=padding.only(left=20, right=20, top=10, bottom=10),
                        width=self.page.width * 0.75,
                        focused_border_color=TERTIARY_COLOR,
                        focused_border_width=2,
                    ),
                    IconButton(
                        icon=ft.icons.SEND,
                        icon_color=TEXT_COLOR,
                        bgcolor=TERTIARY_COLOR,
                        width=50,
                        height=50,
                        icon_size=20,
                        style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ),
                    ),
                ],
                spacing=10,
                alignment="center",
            ),
            margin=margin.only(top=10),
        )


        return Container(
            padding=padding.all(15),
            content=Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            back_button,
                            Text(
                                "Assistant Médical Intelligent" if self.current_language == "fr" else "المساعد الطبي الذكي",
                                size=22,
                                weight="bold"
                            ),
                            Container(width=48),
                        ],
                        width=self.page.width * 0.9,
                    ),

                    Container(
                        content=Text(
                            "Vous pouvez poser n'importe quelle question médicale et l'assistant intelligent y répondra" if self.current_language == "fr" else "يمكنك طرح أي سؤال طبي وسيقوم المساعد الذكي بالإجابة عليه",
                            size=14,
                            color=CONTRAST_COLOR,
                            text_align="center",
                        ),
                        width=self.page.width * 0.9,
                        margin=margin.only(bottom=15),
                    ),
                    chat_messages,
                    suggestions,
                    chat_input,
                ],
            ),
        )

    def build_other_services_view(self):
        """Build the other services view"""

        back_button = IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=PRIMARY_COLOR,
            tooltip=self.translations[self.current_language]["back"],
            on_click=self.go_to_home
        )

        #service cards  language
        if self.current_language == "ar":
            services = [
                {
                    "title": "توصيل الأدوية",
                    "description": "طلب الأدوية وتوصيلها إلى المنزل",
                    "icon": ft.icons.DELIVERY_DINING,
                    "color": "#4299E1",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
                {
                    "title": "استشارات طبية",
                    "description": "تحدث مع طبيب عبر الإنترنت",
                    "icon": ft.icons.HEALTH_AND_SAFETY,
                    "color": "#48BB78",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
                {
                    "title": "تذكير بالأدوية",
                    "description": "تذكير بمواعيد تناول الأدوية",
                    "icon": ft.icons.ALARM,
                    "color": "#ED8936",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
                {
                    "title": "السجل الطبي",
                    "description": "احفظ سجلك الطبي وشاركه مع الأطباء",
                    "icon": ft.icons.FOLDER_SHARED,
                    "color": "#9F7AEA",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
                {
                    "title": "البحث عن المخابر الطببة",
                    "description": "المخابر",
                    "icon": ft.icons.MONITOR_HEART,
                    "color": "#F56565",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
                {
                    "title": "مسح الوصفة الطبية",
                    "description": "كود QR",
                    "icon": ft.icons.QR_CODE,
                    "color": "#347175",
                    "coming_soon": True,
                    "coming_soon_text": "قريباً"
                },
            ]
        else:
            services = [
                {
                    "title": "Livraison de médicaments",
                    "description": "Commandez et faites livrer des médicaments",
                    "icon": ft.icons.DELIVERY_DINING,
                    "color": "#4299E1",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
                {
                    "title": "Consultations médicales",
                    "description": "Parlez à un médecin en ligne",
                    "icon": ft.icons.HEALTH_AND_SAFETY,
                    "color": "#48BB78",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
                {
                    "title": "Rappel de médicaments",
                    "description": "Rappels pour prendre vos médicaments",
                    "icon": ft.icons.ALARM,
                    "color": "#ED8936",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
                {
                    "title": "Dossier médical",
                    "description": "Enregistrez et partagez votre dossier médical",
                    "icon": ft.icons.FOLDER_SHARED,
                    "color": "#9F7AEA",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
                {
                    "title": "Recherche de laboratoires",
                    "description": "Laboratoires médicaux",
                    "icon": ft.icons.MONITOR_HEART,
                    "color": "#F56565",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
                {
                    "title": "Scanner d'ordonnance",
                    "description": "Code QR",
                    "icon": ft.icons.QR_CODE,
                    "color": "#347175",
                    "coming_soon": True,
                    "coming_soon_text": "Bientôt"
                },
            ]

        service_cards = []
        for service in services:
            card = Container(
                width=self.page.width * 0.9,
                height=100,
                border_radius=border_radius.all(15),
                bgcolor=CARD_COLOR,
                padding=padding.all(15),
                margin=margin.only(bottom=15),
                shadow=BoxShadow(
                    spread_radius=0,
                    blur_radius=8,
                    color=SHADOW_COLOR,
                    offset=ft.Offset(0, 2),
                ),
                content=Row(
                    alignment="spaceBetween",
                    vertical_alignment="center",
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    width=50,
                                    height=50,
                                    border_radius=border_radius.all(25),
                                    bgcolor=service["color"],
                                    content=Icon(service["icon"], color=TEXT_COLOR, size=24),
                                    alignment=alignment.center,
                                ),
                                Container(width=15),
                                Column(
                                    spacing=5,
                                    controls=[
                                        Text(service["title"], weight="bold", size=16),
                                        Text(service["description"], color=CONTRAST_COLOR, size=12),
                                        Container(
                                            content=Text(service["coming_soon_text"], color=TEXT_COLOR, size=10),
                                            bgcolor=ACCENT_COLOR,
                                            padding=padding.symmetric(horizontal=8, vertical=2),
                                            border_radius=border_radius.all(10),
                                            visible=service["coming_soon"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Container(
                            content=Icon(ft.icons.ARROW_FORWARD_IOS, size=16, color=CONTRAST_COLOR),
                            padding=padding.all(8),
                            border_radius=border_radius.all(20),
                            bgcolor=ft.colors.with_opacity(0.05, PRIMARY_COLOR),
                        ),
                    ],
                ),
                animate=animation.Animation(300, "decelerate"),
            )
            service_cards.append(card)


        return Container(
            padding=padding.all(15),
            content=Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            back_button,
                            Text(self.translations[self.current_language]["other_services"], size=22, weight="bold"),
                            Container(width=48),
                        ],
                        width=self.page.width * 0.9,
                    ),
                    Container(
                        content=Text(
                            "Services supplémentaires bientôt disponibles" if self.current_language == "fr" else "خدمات إضافية ستكون متاحة قريباً",
                            size=14,
                            color=CONTRAST_COLOR,
                            text_align="center",
                        ),
                        width=self.page.width * 0.9,
                        margin=margin.only(bottom=10),
                    ),
                    *service_cards,
                ],
            ),
        )

    def build_doctors_view(self):
        return Container(
            bgcolor=BACKGROUND_COLOR,
            alignment=alignment.center,
            expand=True,
            padding=padding.all(20),
            content=Column(
                horizontal_alignment="center",
                alignment="center",
                spacing=20,
                controls=[

                    Container(
                        width=120,
                        height=120,
                        border_radius=border_radius.all(60),
                        bgcolor=ft.colors.with_opacity(0.1, PRIMARY_COLOR),
                        content=Container(
                            width=100,
                            height=100,
                            border_radius=border_radius.all(50),
                            bgcolor=ft.colors.with_opacity(0.2, PRIMARY_COLOR),
                            content=Container(
                                width=80,
                                height=80,
                                border_radius=border_radius.all(40),
                                bgcolor=ft.colors.with_opacity(0.3, PRIMARY_COLOR),
                                content=Icon(
                                    ft.icons.MEDICAL_SERVICES,
                                    size=40,
                                    color=PRIMARY_COLOR
                                ),
                                alignment=alignment.center,
                            ),
                            alignment=alignment.center,
                        ),
                        alignment=alignment.center,
                        animate=animation.Animation(1000, "bounceOut"),
                    ),


                    Container(
                        content=Text(
                            "قيد التطوير",
                            size=28,
                            weight="bold",
                            color=PRIMARY_COLOR
                        ),
                        animate=animation.Animation(800, "decelerate"),
                        animate_opacity=400,
                    ),


                    Container(
                        content=Text(
                            "سيتم إضافة هذه الميزة قريباً",
                            color=CONTRAST_COLOR,
                            size=16,
                            text_align="center",
                        ),
                        width=300,
                        animate=animation.Animation(1000, "decelerate"),
                        animate_opacity=600,
                    ),


                    Container(
                        content=Text(
                            "قريباً",
                            color=TEXT_COLOR,
                            size=14,
                            weight="w500",
                        ),
                        bgcolor=ACCENT_COLOR,
                        border_radius=border_radius.all(20),
                        padding=padding.symmetric(horizontal=20, vertical=10),
                        margin=margin.only(top=10),
                        animate=animation.Animation(1200, "bounceOut"),
                    ),
                ],
            ),
        )

    def build_services_view(self):
        #  service cards
        services = [
            {
                "title": "توصيل الأدوية",
                "icon": ft.icons.DELIVERY_DINING,
                "color": "#4299E1",  # Blue
                "coming_soon": True
            },
            {
                "title": "استشارات طبية",
                "icon": ft.icons.HEALTH_AND_SAFETY,
                "color": "#48BB78",  # Green
                "coming_soon": True
            },
            {
                "title": "تذكير بالأدوية",
                "icon": ft.icons.ALARM,
                "color": "#ED8936",  # Orange
                "coming_soon": True
            },
        ]

        service_cards = []
        for service in services:
            card = Container(
                width=self.page.width * 0.9,
                height=100,
                border_radius=border_radius.all(15),
                bgcolor=CARD_COLOR,
                padding=padding.all(15),
                margin=margin.only(bottom=15),
                shadow=BoxShadow(
                    spread_radius=0,
                    blur_radius=8,
                    color=SHADOW_COLOR,
                    offset=ft.Offset(0, 2),
                ),
                content=Row(
                    alignment="spaceBetween",
                    vertical_alignment="center",
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    width=50,
                                    height=50,
                                    border_radius=border_radius.all(25),
                                    bgcolor=service["color"],
                                    content=Icon(service["icon"], color=TEXT_COLOR, size=24),
                                    alignment=alignment.center,
                                ),
                                Container(width=15),  # Spacer
                                Column(
                                    spacing=5,
                                    controls=[
                                        Text(service["title"], weight="bold", size=16),
                                        Text("قريباً", color=CONTRAST_COLOR, size=12),
                                    ],
                                ),
                            ],
                        ),
                        Container(
                            content=Icon(ft.icons.ARROW_FORWARD_IOS, size=16, color=CONTRAST_COLOR),
                            padding=padding.all(8),
                            border_radius=border_radius.all(20),
                            bgcolor=ft.colors.with_opacity(0.05, PRIMARY_COLOR),
                        ),
                    ],
                ),
                animate=animation.Animation(300, "decelerate"),
            )
            service_cards.append(card)

        return Container(
            bgcolor=BACKGROUND_COLOR,
            padding=padding.all(20),
            content=Column(
                horizontal_alignment="center",
                spacing=20,
                controls=[
                    # Header
                    Container(
                        content=Row(
                            alignment="spaceBetween",
                            controls=[
                                Text("الخدمات الإضافية", size=24, weight="bold", color=PRIMARY_COLOR),
                                Container(
                                    content=Icon(ft.icons.MISCELLANEOUS_SERVICES, color=ACCENT_COLOR),
                                    padding=padding.all(8),
                                    border_radius=border_radius.all(20),
                                    bgcolor=ft.colors.with_opacity(0.1, ACCENT_COLOR),
                                ),
                            ],
                        ),
                        margin=margin.only(bottom=10),
                    ),


                    Container(
                        content=Text(
                            "خدمات إضافية ستكون متاحة في المستقبل القريب",
                            color=CONTRAST_COLOR,
                            size=14,
                            text_align="center",
                        ),
                        margin=margin.only(bottom=20),
                    ),


                    *service_cards,


                    Container(
                        content=Text(
                            "المزيد من الخدمات قريباً...",
                            color=CONTRAST_COLOR,
                            italic=True,
                            size=14,
                        ),
                        margin=margin.only(top=10),
                    ),
                ],
            ),
        )

def main(page: Page):

    page.fonts = {
        "ThuluthFont": "assets/font/GE_SS_Unique_Light_1.otf",
    }


    MedicineApp(page)

# Devloped By Fares Benatmane
ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir="assets")
