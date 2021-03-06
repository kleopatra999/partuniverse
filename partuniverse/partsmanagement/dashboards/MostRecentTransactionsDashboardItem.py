# -*- coding: utf-8 -*-
from dashboard.DashboardItemRegistry import DashboardItemRegistry
from dashboard.DashboardItem import DashboardItem
from django.template import RequestContext, loader
from django.utils.safestring import mark_safe
from django.db.models import F
from partsmanagement.models import Transaction


class MostRecentTransactionsDashboardItem(DashboardItem):
    id = "most_recent_transactions"
    name = "Most recent Transactions"
    description = "Display a table with the most recent transactions."

    def render(self):
        # parts = Part.objects.exclude(on_stock__gt='0', on_stock__gte=F('min_stock'))
        transactions = Transaction.objects.order_by('-date')[:5].all()
        template = loader.get_template('dashboard/most_recent_transactions.html')
        context = RequestContext(self.container.request, {
            'transactions': transactions,
        })
        return mark_safe(template.render(context))

DashboardItemRegistry.add(MostRecentTransactionsDashboardItem)
