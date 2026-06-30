import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from recommender import MovieRecommender


class MovieRecommenderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Movie Recommendation System")
        self.root.geometry("760x620")
        self.root.resizable(False, False)

        dataset_path = Path(__file__).parent / "movies.csv"
        self.recommender = MovieRecommender(dataset_path)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🎬 Movie Recommendation System",
            font=("Arial", 22, "bold"),
            fg="#2c3e50",
        )
        title_label.pack(pady=16)

        search_frame = tk.Frame(self.root)
        search_frame.pack(fill="x", padx=20)

        search_label = tk.Label(
            search_frame,
            text="Movie Name",
            font=("Arial", 12, "bold"),
            anchor="w",
            width=12,
        )
        search_label.pack(side="left")

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=40)
        self.search_entry.pack(side="left", padx=(10, 5), pady=4)
        self.search_entry.focus()

        recommend_button = tk.Button(
            search_frame,
            text="Recommend",
            command=self.recommend_movie,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
        )
        recommend_button.pack(side="left", padx=5)

        random_button = tk.Button(
            search_frame,
            text="Random Movie",
            command=self.insert_random_movie,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
        )
        random_button.pack(side="left", padx=5)

        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=20, pady=(10, 0))

        result_label = tk.Label(
            list_frame,
            text="Recommended Movies",
            font=("Arial", 14, "bold"),
            anchor="w",
        )
        result_label.pack(fill="x", pady=(0, 10))

        self.recommendation_box = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            activestyle="none",
            height=18,
            selectbackground="#AED6F1",
            bd=2,
            relief="sunken",
        )
        self.recommendation_box.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.recommendation_box.yview)
        scrollbar.pack(side="left", fill="y")
        self.recommendation_box.configure(yscrollcommand=scrollbar.set)

        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=20, pady=12)

        clear_button = tk.Button(
            control_frame,
            text="Clear",
            command=self.clear_results,
            bg="#f1c40f",
            fg="black",
            font=("Arial", 11, "bold"),
            width=12,
        )
        clear_button.pack(side="left", padx=(0, 10))

        help_button = tk.Button(
            control_frame,
            text="Help",
            command=self.show_help,
            bg="#8e44ad",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
        )
        help_button.pack(side="left", padx=(0, 10))

        about_button = tk.Button(
            control_frame,
            text="About",
            command=self.show_about,
            bg="#34495e",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
        )
        about_button.pack(side="left", padx=(0, 10))

        exit_button = tk.Button(
            control_frame,
            text="Exit",
            command=self.exit_app,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=12,
        )
        exit_button.pack(side="left")

        self.status_label = tk.Label(
            self.root,
            text="Enter a movie name and click Recommend.",
            font=("Arial", 11),
            fg="#555",
            anchor="w",
            justify="left",
        )
        self.status_label.pack(fill="x", padx=20, pady=(0, 10))

        self.root.bind("<Return>", lambda event: self.recommend_movie())

    def insert_random_movie(self):
        random_title = self.recommender.get_random_title()
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, random_title)
        self.status_label.config(text="Random movie selected. Click Recommend to see suggestions.")

    def recommend_movie(self):
        movie_name = self.search_entry.get().strip()
        if not movie_name:
            self.status_label.config(text="Please enter a movie name before recommending.")
            return

        recommendations, matched_title = self.recommender.recommend(movie_name)
        self.recommendation_box.delete(0, tk.END)

        if recommendations is None:
            messagebox.showerror("Movie Not Found", "No matching movie found. Please try another title.")
            self.status_label.config(text="Movie not found. Try a different title or use Random Movie.")
            return

        self.status_label.config(
            text=f"Showing recommendations based on '{matched_title.title()}'."
        )

        for index, movie in enumerate(recommendations, start=1):
            display_text = f"{index}. {movie['title']} ({movie['genre']}) - Rating: {movie['rating']}"
            self.recommendation_box.insert(tk.END, display_text)

    def clear_results(self):
        self.search_entry.delete(0, tk.END)
        self.recommendation_box.delete(0, tk.END)
        self.status_label.config(text="Enter a movie name and click Recommend.")

    def show_help(self):
        messagebox.showinfo(
            "Help",
            "Enter a movie title and click Recommend to see the top 10 similar movies.\n"
            "If the movie name is not found, try a slightly different title or use Random Movie.",
        )

    def show_about(self):
        messagebox.showinfo(
            "About",
            "Movie Recommendation System\n\n"
            "This app uses TF-IDF and cosine similarity to recommend movies based on content features.\n"
            "Built with Python, Tkinter, Pandas, NumPy, and Scikit-learn.",
        )

    def exit_app(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
