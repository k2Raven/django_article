def article_validate(title, content, author):
        errors = {}
        if not title:
            errors['title'] = 'Поле обязательное'
        elif len(title) > 50:
            errors['title'] = 'Максимальная длина 50 символов'

        if not content:
            errors['content'] = 'Поле обязательное'
        elif len(content) > 3000:
            errors['content'] = 'Максимальная длина 3000 символов'

        if not author:
            errors['author'] = 'Поле обязательное'
        elif len(author) > 40:
            errors['author'] = 'Максимальная длина 40 символов'

        return errors