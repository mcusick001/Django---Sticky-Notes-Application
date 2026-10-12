from django.test import TestCase
from django.urls import reverse
from .models import Note

# Create your tests here.


class NoteModelandViewTestCase(TestCase):

    def setUp(self):
        # Create a test note to be used across multiple tests
        self.note = Note.objects.create(
            title="Test Note Title",
            content="This is test note content."
        )

    def test_note_string_representation(self):
        """Test the string representation of the Note model"""
        self.assertEqual(str(self.note), "Test Note Title")

    def test_note_list_view(self):
        """Test the Read (List) view status code and context"""
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note Title")
        self.assertTemplateUsed(response, 'sticky_notes/note_list.html')

    def test_note_detail_view(self):
        """Test the Read (Detail) view for a single note"""
        response = self.client.get(reverse('note-detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is test note content.")
        self.assertTemplateUsed(response, 'sticky_notes/note_detail.html')

    def test_note_create_view_get(self):
        """Test that the create note form page renders successfully"""
        response = self.client.get(reverse('note-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sticky_notes/note_form.html')

    def test_note_create_view_post(self):
        """Test creating a new note via POST request"""
        response = self.client.post(reverse('note-create'), {
            'title': 'New Created Note',
            'content': 'Newly written content.'
        })
        # Check redirection back to the note list after successful creation
        self.assertRedirects(response, reverse('note-list'))
        self.assertEqual(Note.objects.count(), 2)
        self.assertTrue(Note.objects.filter(title='New Created Note').exists())

    def test_note_update_view_post(self):
        """Test updating an existing note via POST request"""
        response = self.client.post(reverse('note-update',
                                            args=[self.note.pk]), {
            'title': 'Updated Title',
            'content': 'Updated content.'
        })
        self.assertRedirects(response, reverse('note-list'))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.content, 'Updated content.')

    def test_note_delete_view_post(self):
        """Test deleting a note via POST request"""
        response = self.client.post(reverse('note-delete',
                                            args=[self.note.pk]))
        self.assertRedirects(response, reverse('note-list'))
        self.assertEqual(Note.objects.count(), 0)
