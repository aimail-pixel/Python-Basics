"Core Basics example: Inheritance, super() & MRO (1)"

def main():
    class Base:
        def title(self):
            return "Course"
    class Lab(Base):
        def title(self):
            return super().title() + " lab"
    print(Lab().title())


if __name__ == "__main__":
    main()
