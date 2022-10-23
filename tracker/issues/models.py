from django.db import models


class Issue(models.Model):

	class Type(models.TextChoices):
		BUG = 'BUG', 'Bug'
		STORY = 'STORY', 'Story'
		TASK = 'TASK', 'Task'
		SUBTASK = 'SUBTASK', 'Sub task'

	class Status(models.TextChoices):
		OPEN = 'OPEN', 'Open'
		IN_PROGRESS = 'IN_PROGRESS', 'In progress'
		RESOLVED = 'RESOLVED', 'Resolved'

	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	summary = models.CharField(max_length=255)
	description = models.TextField()

	type = models.CharField(
		max_length=20,
		choices=Type.choices,
	)
	status = models.CharField(
		max_length=20,
		choices=Status.choices,
	)


class SubIssue(models.Model):
	parent_issue = models.ForeignKey(
		Issue,
		on_delete=models.CASCADE,
		related_name='+',
	)
	sub_issue = models.ForeignKey(
		Issue,
		on_delete=models.CASCADE,
		related_name='+',
	)

	class Meta:
		unique_together = (('parent_issue', 'sub_issue'),)
