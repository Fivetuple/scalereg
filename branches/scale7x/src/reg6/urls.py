from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'scale.reg6.views.index'),
    (r'^add_items/$', 'scale.reg6.views.AddItems'),
    (r'^add_attendee/$', 'scale.reg6.views.AddAttendee'),
    (r'^registered_attendee/$', 'scale.reg6.views.RegisteredAttendee'),
    (r'^start_payment/$', 'scale.reg6.views.StartPayment'),
    (r'^payment/$', 'scale.reg6.views.Payment'),
    (r'^sale/$', 'scale.reg6.views.Sale'),
    (r'^failed_payment/$', 'scale.reg6.views.FailedPayment'),
    (r'^finish_payment/$', 'scale.reg6.views.FinishPayment'),
    (r'^reg_lookup/$', 'scale.reg6.views.RegLookup'),
    (r'^kiosk/$', 'scale.reg6.views.kiosk_index'),
    (r'^checkin/$', 'scale.reg6.views.CheckIn'),
    (r'^finish_checkin/$', 'scale.reg6.views.FinishCheckIn'),
    (r'^redeem_coupon/$', 'scale.reg6.views.RedeemCoupon'),
    (r'^add_coupon/$', 'scale.reg6.views.AddCoupon'),
    (r'^checked_in/$', 'scale.reg6.views.CheckedIn'),
    (r'^mass_add/$', 'scale.reg6.views.MassAdd'),
    (r'^clear_badorder/$', 'scale.reg6.views.ClearBadOrder'),
    (r'^staff/', include('scale.reg6.staff.urls')),
)