from django.shortcuts import render, redirect
import json
from pathlib import Path
from django.http import Http404
from .forms import NewsForm


def load_news():
    path = Path("news/data.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_news(news_list):
    path = Path("news/data.json")
    with open(path, "w", encoding="utf-8") as file:
        json.dump(news_list, file, ensure_ascii=False, indent=4)


def home(request):
    news_list = load_news()
    return render(request, "home.html", {"news_list": news_list})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            author = form.cleaned_data["author"]

            news_list = load_news()

            if news_list:
                ids = [item["id"] for item in news_list]
                new_id = max(ids) + 1
            else:
                new_id = 1

            new_item = {
                "id": new_id,
                "title": title,
                "content": content,
                "author": author
            }

            news_list.append(new_item)
            save_news(news_list)

            return redirect("/")
    else:
        form = NewsForm()

    return render(request, "add_news.html", {"form": form})


def news_detail_view(request, news_id):
    news_list = load_news()

    for item in news_list:
        if item["id"] == news_id:
            return render(request, "news_detail.html", {"news": item})

    raise Http404("Новость не найдена")


def delete_news(request, news_id):
    news_list = load_news()

    news_to_delete = None

    for item in news_list:
        if item["id"] == news_id:
            news_to_delete = item
            break

    if news_to_delete is None:
        raise Http404("Новость не найдена")

    if request.method == "POST":
        news_list.remove(news_to_delete)
        save_news(news_list)
        return redirect("/")

    return render(request, "delete_news.html", {"news": news_to_delete})