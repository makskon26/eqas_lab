import tkinter as tk


class Memento:
    def __init__(self, email, push, sms):
        self.email = email
        self.push = push
        self.sms = sms


class NotificationSettings:
    def __init__(self, email=True, push=False, sms=True):
        self.email = email
        self.push = push
        self.sms = sms

    def create_memento(self):
        return Memento(self.email, self.push, self.sms)

    def restore(self, memento):
        self.email = memento.email
        self.push = memento.push
        self.sms = memento.sms


class NotificationSettingsUI:
    def __init__(self, settings):
        self.settings = settings
        self.master = tk.Tk()
        self.master.title("Notification Settings")

        self.email_var = tk.BooleanVar(value=settings.email)
        self.push_var = tk.BooleanVar(value=settings.push)
        self.sms_var = tk.BooleanVar(value=settings.sms)

        tk.Label(self.master, text="Email Notifications:").grid(row=0, column=0)
        tk.Checkbutton(self.master, variable=self.email_var).grid(row=0, column=1)

        tk.Label(self.master, text="Push Notifications:").grid(row=1, column=0)
        tk.Checkbutton(self.master, variable=self.push_var).grid(row=1, column=1)

        tk.Label(self.master, text="SMS Notifications:").grid(row=2, column=0)
        tk.Checkbutton(self.master, variable=self.sms_var).grid(row=2, column=1)

        tk.Button(self.master, text="Apply", command=self.apply).grid(row=3, column=0)
        tk.Button(self.master, text="Cancel", command=self.cancel, state="disabled").grid(row=3, column=1)

        # Initialize a list to hold the saved mementos
        self.saved_mementos = []
        self.apply_button = None
        self.cancel_button = None

    def _update_buttons_state(self):
        if self.saved_mementos:
            self.apply_button.config(state="normal")
            self.cancel_button.config(state="normal")
        else:
            self.apply_button.config(state="disabled")
            self.cancel_button.config(state="disabled")

    def _update_buttons_state(self):
        if self.saved_mementos:
            self.apply_button.config(state="normal")
            self.cancel_button.config(state="normal")
        else:
            self.apply_button.config(state="disabled")
            self.cancel_button.config(state="disabled")

    def apply(self):
        if self.settings.email != self.email_var.get() or self.settings.push != self.push_var.get() or self.settings.sms != self.sms_var.get():
            # Create a memento before updating settings
            memento = self.settings.create_memento()

            self.settings.email = self.email_var.get()
            self.settings.push = self.push_var.get()
            self.settings.sms = self.sms_var.get()

            # Save the memento to a list of saved mementos
            self.saved_mementos.append(memento)

            # Update the buttons' states
            self._update_buttons_state()

    def cancel(self):
        if self.saved_mementos:
            # Restore the most recently saved memento
            memento = self.saved_mementos.pop()
            self.settings.restore(memento)

            # Update the UI to reflect the restored settings
            self.email_var.set(self.settings.email)
            self.push_var.set(self.settings.push)
            self.sms_var.set(self.settings.sms)

            # Remove the memento from the saved mementos list
            self._update_buttons_state()

        # Enable the "Apply" button after canceling changes
        self.apply_button.config(state="normal")

        # Disable the "Cancel" button after canceling changes
        if not self.saved_mementos:
            self.cancel_button.config(state="disabled")

    def run(self):
        # Add the "Apply" and "Cancel" buttons before the mainloop
        self.apply_button = tk.Button(self.master, text="Apply", command=self.apply)
        self.apply_button.grid(row=3, column=0)

        self.cancel_button = tk.Button(self.master, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=3, column=1)

        # Disable the "Cancel" button by default
        self.cancel_button.config(state="disabled")

        self.master.mainloop()

        print("Email Notifications: ", settings.email)
        print("Push Notifications: ", settings.push)
        print("SMS Notifications: ", settings.sms)


if __name__ == '__main__':
    settings = NotificationSettings()
    ui = NotificationSettingsUI(settings)
    ui.run()

    print("Email Notifications: ", settings.email)
    print("Push Notifications: ", settings.push)
    print("SMS Notifications: ", settings.sms)