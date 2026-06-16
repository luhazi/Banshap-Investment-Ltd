#!/usr/bin/env python3
"""
BANSHAP INVESTMENT COMPANY LIMITED
Premium Investor-Grade Company Profile PDF
Deloitte / McKinsey aesthetic
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
import os

# ── BRAND COLORS ──────────────────────────────────────────────────────────────
NAVY    = HexColor('#0B1F3A')
NAVY2   = HexColor('#0D2848')
NAVY3   = HexColor('#112238')
ROYAL   = HexColor('#1E5EFF')
ROYALD  = HexColor('#1547CC')
GOLD    = HexColor('#C9A227')
GOLDD   = HexColor('#A07820')
LGRAY   = HexColor('#F5F7FA')
MGRAY   = HexColor('#64748B')
DGRAY   = HexColor('#2B2B2B')
BORDER  = HexColor('#E2E8F0')
WHITE   = HexColor('#FFFFFF')
LBLUE   = HexColor('#B8D0F0')
DIVIDER = HexColor('#2A4E7A')

W, H = A4
M = 20 * mm
IW = W - 2 * M

# ── STYLES ────────────────────────────────────────────────────────────────────
def ps(name, **kw):
    return ParagraphStyle(name, **kw)

S = {
    'body':      ps('body',     fontName='Helvetica',      fontSize=9.5,  textColor=DGRAY,  leading=15,   spaceAfter=5,  alignment=TA_JUSTIFY),
    'bodyW':     ps('bodyW',    fontName='Helvetica',      fontSize=9.5,  textColor=WHITE,  leading=15,   spaceAfter=5,  alignment=TA_JUSTIFY),
    'bodyG':     ps('bodyG',    fontName='Helvetica',      fontSize=9.5,  textColor=MGRAY,  leading=14,   spaceAfter=4),
    'secLabel':  ps('secLabel', fontName='Helvetica-Bold', fontSize=7.5,  textColor=GOLD,   letterSpacing=2, spaceAfter=2),
    'secTitle':  ps('secTitle', fontName='Helvetica-Bold', fontSize=21,   textColor=NAVY,   leading=27,   spaceAfter=3),
    'secSub':    ps('secSub',   fontName='Helvetica',      fontSize=10.5, textColor=MGRAY,  leading=16,   spaceAfter=10),
    'h2':        ps('h2',       fontName='Helvetica-Bold', fontSize=13,   textColor=NAVY,   spaceBefore=8, spaceAfter=4),
    'h3':        ps('h3',       fontName='Helvetica-Bold', fontSize=10.5, textColor=NAVY,   spaceAfter=2),
    'h3W':       ps('h3W',      fontName='Helvetica-Bold', fontSize=10.5, textColor=WHITE,  spaceAfter=2),
    'h3G':       ps('h3G',      fontName='Helvetica-Bold', fontSize=10.5, textColor=GOLD,   spaceAfter=2),
    'h3R':       ps('h3R',      fontName='Helvetica-Bold', fontSize=10.5, textColor=ROYAL,  spaceAfter=2),
    'italic':    ps('italic',   fontName='Helvetica-Oblique', fontSize=9.5, textColor=ROYAL, spaceAfter=3),
    'card':      ps('card',     fontName='Helvetica',      fontSize=8.5,  textColor=MGRAY,  leading=13,   spaceAfter=2),
    'cardW':     ps('cardW',    fontName='Helvetica',      fontSize=8.5,  textColor=LBLUE,  leading=13,   spaceAfter=2),
    'bullet':    ps('bullet',   fontName='Helvetica',      fontSize=8.5,  textColor=MGRAY,  leading=13,   spaceAfter=2,  leftIndent=10, bulletIndent=2, bulletText='>'),
    'bulletW':   ps('bulletW',  fontName='Helvetica',      fontSize=8.5,  textColor=WHITE,  leading=13,   spaceAfter=2,  leftIndent=10, bulletIndent=2, bulletText='>'),
    'quote':     ps('quote',    fontName='Helvetica-Oblique', fontSize=10.5, textColor=WHITE, leading=17, spaceAfter=5, alignment=TA_JUSTIFY),
    'qAttr':     ps('qAttr',    fontName='Helvetica-Bold', fontSize=8.5,  textColor=GOLD,   spaceAfter=1),
    'qRole':     ps('qRole',    fontName='Helvetica',      fontSize=8,    textColor=LBLUE),
    'kpiNum':    ps('kpiNum',   fontName='Helvetica-Bold', fontSize=22,   textColor=GOLD,   leading=26,   alignment=TA_CENTER),
    'kpiLbl':    ps('kpiLbl',   fontName='Helvetica',      fontSize=7.5,  textColor=MGRAY,  alignment=TA_CENTER, leading=11),
    'kpiLblW':   ps('kpiLblW',  fontName='Helvetica',      fontSize=7.5,  textColor=LBLUE,  alignment=TA_CENTER, leading=11),
    'teamName':  ps('teamName', fontName='Helvetica-Bold', fontSize=10,   textColor=NAVY,   spaceAfter=1),
    'teamRole':  ps('teamRole', fontName='Helvetica-Bold', fontSize=8.5,  textColor=ROYAL,  spaceAfter=3),
    'teamBio':   ps('teamBio',  fontName='Helvetica',      fontSize=8,    textColor=MGRAY,  leading=12),
    'teamInit':  ps('teamInit', fontName='Helvetica-Bold', fontSize=15,   textColor=WHITE,  alignment=TA_CENTER),
    'ctaLabel':  ps('ctaLabel', fontName='Helvetica-Bold', fontSize=7.5,  textColor=GOLD,   letterSpacing=1, spaceAfter=2),
    'ctaVal':    ps('ctaVal',   fontName='Helvetica',      fontSize=9.5,  textColor=WHITE,  leading=14,   spaceAfter=5),
    'stepTitle': ps('stepTitle',fontName='Helvetica-Bold', fontSize=10,   textColor=NAVY,   spaceAfter=3),
    'stepBody':  ps('stepBody', fontName='Helvetica',      fontSize=8.5,  textColor=MGRAY,  leading=13),
    'trustLbl':  ps('trustLbl', fontName='Helvetica-Bold', fontSize=8.5,  textColor=NAVY,   alignment=TA_CENTER, spaceAfter=2),
    'trustDesc': ps('trustDesc',fontName='Helvetica',      fontSize=7.5,  textColor=MGRAY,  leading=11,   alignment=TA_CENTER),
    'catHead':   ps('catHead',  fontName='Helvetica-Bold', fontSize=10,   textColor=WHITE,  alignment=TA_CENTER),
    'caption':   ps('caption',  fontName='Helvetica',      fontSize=7.5,  textColor=MGRAY,  leading=11),
    'captionB':  ps('captionB', fontName='Helvetica-Bold', fontSize=7.5,  textColor=NAVY),
    'mini':      ps('mini',     fontName='Helvetica',      fontSize=7,    textColor=MGRAY,  leading=10),
}


# ── PAGE CALLBACKS ────────────────────────────────────────────────────────────
def draw_cover(cv, doc):
    cv.saveState()
    cv.setFillColor(NAVY)
    cv.rect(0, 0, W, H, fill=1, stroke=0)
    cv.setFillColor(NAVY2)
    cv.circle(W + 12*mm, H - 8*mm, 100*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#0F2748'))
    cv.circle(W * 0.90, H * 0.18, 45*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#081828'))
    cv.circle(-25*mm, 35*mm, 55*mm, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.rect(0, H - 4*mm, W, 4*mm, fill=1, stroke=0)
    cv.rect(0, 0, W, 2*mm, fill=1, stroke=0)
    cv.setFillColor(GOLDD)
    cv.rect(0, H * 0.52, 4*mm, H * 0.32, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.rect(0, H * 0.52, 2.5*mm, H * 0.32, fill=1, stroke=0)
    bx, by = M, H - 28*mm
    cv.setFillColor(GOLD)
    cv.circle(bx + 7*mm, by + 7*mm, 7.5*mm, fill=1, stroke=0)
    cv.setFillColor(NAVY)
    cv.setFont('Helvetica-Bold', 12)
    cv.drawCentredString(bx + 7*mm, by + 4.5*mm, 'B')
    cv.setFillColor(WHITE)
    cv.setFont('Helvetica-Bold', 9)
    cv.drawString(bx + 19*mm, by + 10*mm, 'BANSHAP')
    cv.setFillColor(LBLUE)
    cv.setFont('Helvetica', 7.5)
    cv.drawString(bx + 19*mm, by + 5*mm, 'INVESTMENT COMPANY LIMITED')
    cv.setFillColor(HexColor('#0D2848'))
    cv.roundRect(W - M - 28*mm, by, 28*mm, 18*mm, 4, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.setFont('Helvetica-Bold', 7)
    cv.drawCentredString(W - M - 14*mm, by + 12*mm, 'EST.')
    cv.setFillColor(WHITE)
    cv.setFont('Helvetica-Bold', 13)
    cv.drawCentredString(W - M - 14*mm, by + 5*mm, '2010')
    cv.setStrokeColor(GOLD)
    cv.setLineWidth(1.5)
    cv.line(M, H * 0.685, W - M, H * 0.685)
    cv.setFillColor(GOLD)
    cv.setFont('Helvetica-Bold', 7.5)
    cv.drawString(M, H * 0.70, 'COMPANY PROFILE  2025')
    cv.setFillColor(WHITE)
    cv.setFont('Helvetica-Bold', 38)
    cv.drawString(M, H * 0.605, 'BANSHAP')
    cv.setFont('Helvetica-Bold', 21)
    cv.drawString(M, H * 0.555, 'INVESTMENT COMPANY')
    cv.drawString(M, H * 0.510, 'LIMITED')
    cv.setFillColor(GOLD)
    cv.rect(M, H * 0.498, 42*mm, 2*mm, fill=1, stroke=0)
    cv.setFillColor(LBLUE)
    cv.setFont('Helvetica', 12)
    cv.drawString(M, H * 0.455, "Tanzania's Trusted Partner for Logistics,")
    cv.drawString(M, H * 0.415, "Compliance & Business Solutions")
    kpi_y = H * 0.195
    kpi_h = H * 0.145
    cv.setFillColor(ROYAL)
    cv.roundRect(M, kpi_y, IW, kpi_h, 7, fill=1, stroke=0)
    cv.setStrokeColor(DIVIDER)
    cv.setLineWidth(0.5)
    for i in range(1, 4):
        x = M + IW * i / 4
        cv.line(x, kpi_y + 5*mm, x, kpi_y + kpi_h - 5*mm)
    kpis = [('15+', 'Years Experience'), ('500+', 'Clients Served'),
            ('26', 'Regions Covered'), ('98%', 'Client Satisfaction')]
    for i, (num, label) in enumerate(kpis):
        cx = M + IW * (i + 0.5) / 4
        cv.setFillColor(GOLD)
        cv.setFont('Helvetica-Bold', 23)
        cv.drawCentredString(cx, kpi_y + kpi_h * 0.55, num)
        cv.setFillColor(LBLUE)
        cv.setFont('Helvetica', 8)
        cv.drawCentredString(cx, kpi_y + kpi_h * 0.22, label)
    cv.setFillColor(MGRAY)
    cv.setFont('Helvetica', 6.5)
    cv.drawCentredString(W/2, 8*mm, 'CONFIDENTIAL  -  FOR CLIENT USE ONLY')
    cv.drawCentredString(W/2, 4.5*mm, 'Banshap Investment Company Limited  -  Dar es Salaam, Tanzania')
    cv.restoreState()


def draw_interior(cv, doc):
    cv.saveState()
    cv.setFillColor(NAVY)
    cv.rect(0, H - 14*mm, W, 14*mm, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.rect(0, H - 14.5*mm, W, 0.5*mm, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.setFont('Helvetica-Bold', 7)
    cv.drawString(M, H - 8.5*mm, 'BANSHAP')
    cv.setFillColor(WHITE)
    cv.setFont('Helvetica', 7)
    cv.drawString(M + 18*mm, H - 8.5*mm, 'INVESTMENT COMPANY LIMITED')
    cv.setFillColor(LBLUE)
    cv.setFont('Helvetica', 7)
    cv.drawRightString(W - M, H - 8.5*mm, 'Company Profile 2025  -  Page %d' % doc.page)
    cv.setFillColor(NAVY)
    cv.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    cv.setFillColor(GOLD)
    cv.rect(0, 10*mm, W, 0.5*mm, fill=1, stroke=0)
    cv.setFillColor(HexColor('#607090'))
    cv.setFont('Helvetica', 6.5)
    cv.drawString(M, 3.8*mm, 'Mkwepu & Samora St, Samora Ave, Dar es Salaam  -  +255 716 628 867  -  sharifu.mtuta@banshapinvestment.co.tz')
    cv.setFillColor(GOLD)
    cv.setFont('Helvetica-Bold', 7)
    cv.drawRightString(W - M, 3.8*mm, 'www.banshapinvestment.co.tz')
    cv.restoreState()


def page_cb(cv, doc):
    if doc.page == 1:
        draw_cover(cv, doc)
    else:
        draw_interior(cv, doc)


# ── HELPERS ───────────────────────────────────────────────────────────────────
def rule(color=GOLD, thickness=2, width=None):
    from reportlab.platypus import HRFlowable
    return HRFlowable(width=width or IW, thickness=thickness, color=color, spaceAfter=0, spaceBefore=0)

def section_header(label, title, subtitle=None):
    out = [
        Paragraph(label, S['secLabel']),
        Paragraph(title, S['secTitle']),
        rule(GOLD, 2),
        Spacer(1, 4*mm),
    ]
    if subtitle:
        out.insert(3, Paragraph(subtitle, S['secSub']))
    return out

def make_kpi_row(items, bg=NAVY, num_style='kpiNum', lbl_style='kpiLblW'):
    col_w = [IW / len(items)] * len(items)
    t = Table([[Paragraph(n, S[num_style]) for n,l in items],
               [Paragraph(l, S[lbl_style]) for n,l in items]],
              colWidths=col_w)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 10),
        ('TOPPADDING', (0,1), (-1,1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('ROUNDEDCORNERS', [7]),
    ]))
    return t

def service_card(num_str, title, value_stmt, bullets, width):
    num_cell = Table([[Paragraph('<b>%s</b>' % num_str, ps('_sn2', fontName='Helvetica-Bold', fontSize=9,
              textColor=NAVY, alignment=TA_CENTER))]],
              colWidths=[8*mm], rowHeights=[8*mm])
    num_cell.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), GOLD),
        ('TOPPADDING', (0,0), (0,0), 4), ('BOTTOMPADDING', (0,0), (0,0), 4),
        ('LEFTPADDING', (0,0), (0,0), 2), ('RIGHTPADDING', (0,0), (0,0), 2),
        ('ROUNDEDCORNERS', [3]),
    ]))
    right_col = [Paragraph(title, S['h3']), Paragraph(value_stmt, S['italic'])] + \
                [Paragraph(b, S['bullet']) for b in bullets]
    t = Table([[num_cell, right_col]], colWidths=[13*mm, width - 13*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('BACKGROUND', (0,0), (-1,-1), LGRAY),
        ('LINEBEFORE', (0,0), (0,-1), 3, GOLD),
        ('GRID', (0,0), (-1,-1), 0.25, BORDER),
    ]))
    return t

def category_header(label, width=IW):
    t = Table([[Paragraph(label, S['catHead'])]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('LINEBEFORE', (0,0), (0,-1), 4, GOLD),
    ]))
    return t

def advantage_card(num, title, body, kpi=None, width=None):
    w = width or (IW / 2 - 3*mm)
    inner = [
        Paragraph('<font color="#C9A227"><b>%s</b></font>  %s' % (num, title),
                  ps('_at', fontName='Helvetica-Bold', fontSize=10, textColor=NAVY, spaceAfter=3, leading=14)),
        Paragraph(body, S['card']),
    ]
    if kpi:
        inner.append(Paragraph(kpi, ps('_kpi', fontName='Helvetica-Bold', fontSize=11, textColor=ROYAL,
                                       spaceBefore=4, spaceAfter=0)))
    t = Table([[inner]], colWidths=[w])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LGRAY),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('GRID', (0,0), (-1,-1), 0.25, BORDER),
        ('LINEBEFORE', (0,0), (0,-1), 3, GOLD),
    ]))
    return t

def testimonial_card(quote, name, role, company, width=IW):
    content = [
        Paragraph('"' + quote + '"', S['quote']),
        Paragraph(name, S['qAttr']),
        Paragraph('%s  -  %s' % (role, company), S['qRole']),
    ]
    t = Table([[content]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
        ('TOPPADDING', (0,0), (-1,-1), 16),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
        ('ROUNDEDCORNERS', [6]),
        ('LINEBEFORE', (0,0), (0,-1), 5, GOLD),
    ]))
    return t

def team_card(name, role, bio, width):
    initials = ''.join(w[0].upper() for w in name.split()[:2])
    init_p = Paragraph(initials, S['teamInit'])
    init_t = Table([[init_p]], colWidths=[11*mm], rowHeights=[11*mm])
    init_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), NAVY),
        ('TOPPADDING', (0,0), (0,0), 5),
        ('BOTTOMPADDING', (0,0), (0,0), 5),
        ('LEFTPADDING', (0,0), (0,0), 2),
        ('RIGHTPADDING', (0,0), (0,0), 2),
        ('ROUNDEDCORNERS', [5]),
    ]))
    right = [Paragraph(name, S['teamName']), Paragraph(role, S['teamRole']),
             Paragraph(bio, S['teamBio'])]
    inner = Table([[init_t, right]], colWidths=[15*mm, width - 19*mm])
    inner.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    outer = Table([[inner]], colWidths=[width])
    outer.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LGRAY),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.25, BORDER),
    ]))
    return outer

# ── STORY BUILDER ─────────────────────────────────────────────────────────────
story = []

# PAGE 1 — COVER
story.append(PageBreak())

# PAGE 2 — COMPANY OVERVIEW
story += section_header('01  COMPANY OVERVIEW', 'Who We Are',
    "Fifteen years of operational excellence building Tanzania's business future from Dar es Salaam outward.")

left_col = [
    Paragraph('<b>Founded in 2010</b>, Banshap Investment Company Limited was established with a single, clear purpose: '
              'to eliminate the operational friction that slows business growth in Tanzania. What began as a logistics '
              'coordination firm has grown into a fully integrated business facilitation company serving hundreds of '
              'clients across all major sectors.', S['body']),
    Spacer(1, 4*mm),
    Paragraph("Today, from our Samora Avenue offices at the heart of Dar es Salaam's commercial district, we provide "
              'comprehensive services spanning freight, regulatory compliance, company registration, investment advisory, '
              'and agricultural supply chains. We bring the same world-class standard of delivery to every client, '
              'regardless of size or sector.', S['body']),
    Spacer(1, 6*mm),
    Table([
        [Paragraph('v', ps('_ck', fontName='Helvetica-Bold', fontSize=10, textColor=GOLD)),
         Paragraph('Fully registered with BRELA, TRA, and all applicable regulatory bodies', S['card'])],
        [Paragraph('v', ps('_ck2', fontName='Helvetica-Bold', fontSize=10, textColor=GOLD)),
         Paragraph('Active operations across all 26 regions of Tanzania', S['card'])],
        [Paragraph('v', ps('_ck3', fontName='Helvetica-Bold', fontSize=10, textColor=GOLD)),
         Paragraph('Serving domestic and international clients since 2010', S['card'])],
        [Paragraph('v', ps('_ck4', fontName='Helvetica-Bold', fontSize=10, textColor=GOLD)),
         Paragraph('98% client satisfaction rate across all service lines', S['card'])],
    ], colWidths=[8*mm, (IW*0.55) - 8*mm]),
]

right_t = Table([[
    Paragraph('"Our mission is to eliminate operational friction for businesses across Tanzania - '
              'connecting reliable logistics infrastructure with expert regulatory support to '
              'accelerate growth at every stage."', S['quote']),
]], colWidths=[IW * 0.38])
right_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), NAVY),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('ROUNDEDCORNERS', [6]),
    ('LINEBEFORE', (0,0), (0,-1), 4, GOLD),
]))

overview_table = Table([[left_col, right_t]], colWidths=[IW * 0.57, IW * 0.43], spaceAfter=6*mm)
overview_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (0,-1), 8),
    ('RIGHTPADDING', (-1,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0),
]))
story.append(overview_table)
story.append(Spacer(1, 4*mm))
story.append(make_kpi_row([('15+', 'Years of Excellence'), ('500+', 'Businesses Served'),
                            ('26', 'Regions Covered'), ('98%', 'Client Satisfaction')]))
story.append(PageBreak())

# PAGE 3 — MISSION / VISION / VALUES
story += section_header('02  OUR FOUNDATION', 'Mission, Vision & Values',
    'The four pillars that define how every member of the Banshap team approaches their work.')

mvn = Table([[
    [Paragraph('OUR MISSION', S['secLabel']),
     Paragraph('Eliminate Operational Friction', S['h3W']),
     Spacer(1, 3*mm),
     Paragraph('To eliminate operational friction for businesses across Tanzania - connecting reliable '
               'logistics infrastructure with expert regulatory support to accelerate growth at every '
               'stage of the business lifecycle.', S['bodyW'])],
    [Paragraph('OUR VISION', S['secLabel']),
     Paragraph("East Africa's Most Trusted Partner", S['h3W']),
     Spacer(1, 3*mm),
     Paragraph('To be East Africa\'s most trusted integrated business facilitation company - recognised '
               'for operational reliability, regulatory integrity, and the measurable commercial outcomes '
               'we deliver for every client we serve.', S['bodyW'])],
]], colWidths=[IW/2 - 3*mm, IW/2 - 3*mm])
mvn.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), NAVY),
    ('BACKGROUND', (1,0), (1,-1), ROYAL),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('ROUNDEDCORNERS', [6]),
]))
story.append(mvn)
story.append(Spacer(1, 6*mm))

qs = Table([[
    Paragraph('QUALITY STATEMENT', S['secLabel']),
    Paragraph('"Quality is What We Provide" - Banshap Investment Company is fully committed to delivering '
              'services that meet and exceed client expectations. This commitment is embedded in every process '
              'we run, every deadline we meet, and every outcome we deliver.', S['bodyW']),
]], colWidths=[36*mm, IW - 36*mm])
qs.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), NAVY3),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('ROUNDEDCORNERS', [5]),
    ('LINEBEFORE', (1,0), (1,-1), 4, GOLD),
]))
story.append(qs)
story.append(Spacer(1, 6*mm))

vals = [
    ('01', 'Integrity', 'Complete transparency in pricing, timelines, and outcomes. Clients receive honest assessments, not optimistic estimates.'),
    ('02', 'Reliability', 'We deliver what we commit to - on time, every time. Our systems are built to maintain performance under any pressure.'),
    ('03', 'Client Partnership', "We invest in understanding clients' long-term goals, building relationships that extend well beyond individual engagements."),
    ('04', 'Operational Excellence', 'Every process is designed, measured, and continuously improved - structured quality management applied to every service line.'),
    ('05', 'Nationwide Reach', 'The same quality of service from Dar es Salaam to Mtwara, from Arusha to Kigoma - consistent, reliable, everywhere.'),
    ('06', 'Continuous Improvement', 'Active investment in our people, technology, and processes - staying ahead of regulatory and logistics trends.'),
]
val_cells = []
for num, title, body in vals:
    val_cells.append([
        Paragraph('<font color="#C9A227"><b>%s</b></font>' % num, ps('_vn', fontName='Helvetica-Bold', fontSize=13, textColor=GOLD, leading=16, spaceAfter=3)),
        Paragraph(title, S['h3']),
        Paragraph(body, S['card']),
    ])

val_rows = [val_cells[i:i+3] for i in range(0, len(val_cells), 3)]
vt = Table(val_rows, colWidths=[IW/3]*3)
vt.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), LGRAY),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.3, BORDER),
]))
story.append(vt)
story.append(PageBreak())

# PAGES 4-5 — SERVICES
story += section_header('03  OUR SERVICES', 'Comprehensive Business Solutions',
    'Nine integrated service lines covering every operational, regulatory, and logistical need across Tanzania.')

story.append(KeepTogether([category_header('A  -  LOGISTICS & TRANSPORT SERVICES'), Spacer(1, 3*mm)]))
svc_a = [
    ('01', 'Logistics & Freight Infrastructure', 'End-to-end supply chain management across Tanzania - delivered with precision.',
     ['Nationwide haulage on Northern, Central, and TAZARA corridors', 'Port clearance and customs documentation management', 'Warehousing in Dar es Salaam, Arusha, and Mwanza', 'Real-time GPS cargo tracking with client portal', '24/7 operations centre for critical escalations']),
    ('02', 'Cargo Transportation', 'Reliable, time-bound freight delivery for all cargo types across East Africa.',
     ['Heavy commercial fleet for bulk and break-bulk freight', 'Temperature-controlled transport for perishables', 'Cross-border freight (Tanzania, Kenya, Uganda)', 'Load consolidation for cost-efficient SME logistics']),
    ('03', 'Vehicle Registration & SUMATRA Compliance', 'Complete fleet documentation - keeping vehicles road-legal and insured.',
     ['SUMATRA licence procurement and annual renewal', 'Vehicle inspection scheduling and certification', 'Fleet documentation management and tracking', 'Third-party liability insurance coordination']),
]
left_svc_a = [service_card(*svc_a[0], width=IW/2 - 3*mm), Spacer(1, 4*mm), service_card(*svc_a[2], width=IW/2 - 3*mm)]
right_svc_a = [service_card(*svc_a[1], width=IW/2 - 3*mm)]
svc_a_t = Table([[left_svc_a, right_svc_a]], colWidths=[IW/2 - 3*mm, IW/2 - 3*mm])
svc_a_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (0,-1), 6), ('RIGHTPADDING', (-1,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
story.append(svc_a_t)
story.append(Spacer(1, 6*mm))

story.append(KeepTogether([category_header('B  -  REGULATORY & COMPLIANCE SERVICES'), Spacer(1, 3*mm)]))
svc_b = [
    ('04', 'BRELA Company Registration', 'From name search to certificate of incorporation - completed in as few as 3 business days.',
     ['Company name search and reservation', 'Memorandum and articles of association drafting', 'Certificate of incorporation delivery', 'Foreign branch and NGO registration', 'Annual returns filing with BRELA']),
    ('05', 'Business Licensing Services', 'Multi-agency licence procurement across 12 industry sectors, managed end-to-end.',
     ['Licences from TBS, TFDA, SUMATRA, NEMC, and local authorities', 'Annual licence renewal with deadline tracking', 'Sector licence audits and gap analysis', 'Fire, safety, and environmental compliance']),
    ('06', 'Annual Returns & Tax Filing', 'Full TRA compliance by CPA-T qualified tax professionals - zero penalties, zero surprises.',
     ['Corporate income tax and VAT return preparation', 'TIN and VAT registration for new entities', 'EFD machine procurement and TRA registration', 'TRA audit representation and advisory']),
]
svc_b_cards = [service_card(*s, width=IW/3 - 4*mm) for s in svc_b]
svc_b_t = Table([svc_b_cards], colWidths=[IW/3 - 4*mm]*3)
svc_b_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (0,0), 4), ('RIGHTPADDING', (0,0), (1,0), 4), ('RIGHTPADDING', (-1,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
story.append(svc_b_t)
story.append(PageBreak())

story += section_header('03  OUR SERVICES (CONTINUED)', 'Business & Advisory Solutions',
    'Strategic advisory, agricultural supply chains, and corporate procurement - all under one roof.')
story.append(KeepTogether([category_header('C  -  BUSINESS & ADVISORY SERVICES'), Spacer(1, 3*mm)]))
svc_c = [
    ('07', 'Investment & Corporate Advisory', "Guiding domestic and foreign investors through Tanzania's dynamic commercial environment.",
     ['Market entry strategy and sector feasibility analysis', 'Company structuring and shareholder agreements', 'Regulatory roadmap for foreign direct investment', 'Ongoing operational and compliance advisory']),
    ('08', 'Agricultural Inputs & Supplies', 'Certified agri-inputs delivered to farming enterprises and cooperatives nationwide.',
     ['TOSCI-certified seed varieties for food and cash crops', 'TFRA-licensed agrochemical distribution', 'Bulk fertiliser and irrigation equipment supply', 'Delivery to cooperative warehouses nationwide']),
    ('09', 'General Supplies & Procurement', 'Corporate procurement delivered with verified documentation and competitive pricing.',
     ['Office equipment and IT hardware procurement', 'Industrial consumables and institutional supplies', 'Full procurement documentation and delivery tracking', 'Framework agreements for recurring needs']),
]
svc_c_cards = [service_card(*s, width=IW/3 - 4*mm) for s in svc_c]
svc_c_t = Table([svc_c_cards], colWidths=[IW/3 - 4*mm]*3)
svc_c_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (0,0), 4), ('RIGHTPADDING', (0,0), (1,0), 4), ('RIGHTPADDING', (-1,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
story.append(svc_c_t)
story.append(Spacer(1, 8*mm))
story.append(make_kpi_row([('9', 'Service Lines'), ('12+', 'Sectors Covered'), ('3', 'Business Days BRELA'), ('24/7', 'Logistics Support')], bg=ROYAL))
story.append(PageBreak())

# PAGE 6 — WHY CHOOSE US
story += section_header('04  THE BANSHAP ADVANTAGE', 'Why Choose Us?',
    'We combine operational depth with regulatory expertise to deliver outcomes independent providers cannot match.')
advs = [
    ('01', 'Operational Reliability', 'Our logistics fleet and regulatory teams maintain 98.4% on-time performance across all active engagements, backed by real-time tracking and proactive client communication.', 'On-Time Performance: 98.4%'),
    ('02', 'Fast Execution', 'Standard BRELA registrations completed in 3 business days. Licence applications tracked daily. Logistics dispatched within 4 hours of confirmed booking.', 'BRELA Reg. In: 3 Business Days'),
    ('03', 'Regulatory Expertise', 'Deep working relationships with BRELA, TRA, TFDA, TBS, SUMATRA, and NEMC enable us to navigate complex multi-agency applications faster than any competitor.', 'Agencies Covered: 6+'),
    ('04', 'Professional Advisory Team', "Our team includes CPA-T certified accountants, compliance specialists, and logistics planners with collective experience spanning 15+ years of Tanzania's commercial environment.", 'Combined Experience: 15+ Years'),
    ('05', 'Nationwide Coverage', 'Active operations in Dar es Salaam, Dodoma, Mwanza, Arusha, Mbeya, and Zanzibar - with an established agent network covering all 26 regions of Tanzania.', 'Coverage: All 26 Regions'),
    ('06', 'Dedicated Account Management', 'Every client is assigned a dedicated account manager available Monday to Saturday. Critical logistics receive 24/7 escalation support.', 'Account Support: Mon-Sat + 24/7'),
]
adv_rows = []
for i in range(0, len(advs), 2):
    row = [advantage_card(*advs[i]), advantage_card(*advs[i+1]) if i+1 < len(advs) else Spacer(1,1)]
    adv_rows.append(row)
adv_t = Table(adv_rows, colWidths=[IW/2 - 3*mm, IW/2 - 3*mm], spaceAfter=6*mm)
adv_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (0,-1), 5), ('RIGHTPADDING', (-1,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
story.append(adv_t)
story.append(Paragraph('TRUSTED BY LEADING ORGANISATIONS', S['secLabel']))
story.append(Spacer(1, 3*mm))
partners = ['CRDB Bank', 'NMB Bank', 'Vodacom TZ', 'Azam Group', 'TANESCO', 'TPA', 'TRA', 'Watu Credit', 'Stanbic Bank', 'TBL']
p_cells = [Paragraph('<b>%s</b>' % p, ps('_pc', fontName='Helvetica-Bold', fontSize=8, textColor=NAVY, alignment=TA_CENTER)) for p in partners]
p_t = Table([p_cells[:5], p_cells[5:]], colWidths=[IW/5]*5)
p_t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), LGRAY), ('GRID', (0,0), (-1,-1), 0.3, BORDER), ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('TOPPADDING', (0,0), (-1,-1), 9), ('BOTTOMPADDING', (0,0), (-1,-1), 9)]))
story.append(p_t)
story.append(PageBreak())

# PAGE 7 — PROCESS FLOW
story += section_header('05  HOW WE WORK', 'Our 4-Step Engagement Process',
    'A streamlined model designed to deliver results quickly - with full transparency at every stage.')
steps = [
    ('01', 'Consultation', 'No-obligation meeting to understand your requirements, timeline, and business objectives - in person or via video call.', ['Needs assessment', 'Timeline scoping', 'No-obligation meeting']),
    ('02', 'Assessment & Planning', 'Our specialists assess documentation, regulatory status, and operational requirements - then deliver a clear action plan.', ['Documentation review', 'Action plan with milestones', 'Transparent cost structure']),
    ('03', 'Execution', 'Our dedicated team submits applications, coordinates logistics, and manages all agency interactions on your behalf.', ['Daily status updates', 'Multi-agency coordination', 'Dedicated account manager']),
    ('04', 'Delivery & Support', 'All documentation and operational handovers are delivered - followed by ongoing compliance and operational support.', ['Certificate & document delivery', 'Ongoing compliance support', 'Renewal reminders']),
]
step_cells = []
for num, title, body, bpts in steps:
    num_block = Table([[Paragraph(num, ps('_pn', fontName='Helvetica-Bold', fontSize=16, textColor=WHITE, alignment=TA_CENTER))]], colWidths=[12*mm], rowHeights=[12*mm])
    num_block.setStyle(TableStyle([('BACKGROUND', (0,0), (0,0), GOLD), ('TOPPADDING', (0,0), (0,0), 6), ('BOTTOMPADDING', (0,0), (0,0), 6), ('LEFTPADDING', (0,0), (0,0), 2), ('RIGHTPADDING', (0,0), (0,0), 2), ('ROUNDEDCORNERS', [5])]))
    step_cells.append([num_block, Spacer(1, 4*mm), Paragraph(title, S['stepTitle']), Paragraph(body, S['stepBody']), Spacer(1, 3*mm)] + [Paragraph(b, S['bullet']) for b in bpts])

def arrow_cell():
    a = Table([[Paragraph('>', ps('_ar', fontName='Helvetica-Bold', fontSize=22, textColor=GOLD, alignment=TA_CENTER))]], colWidths=[8*mm])
    a.setStyle(TableStyle([('TOPPADDING', (0,0), (0,0), 40), ('LEFTPADDING', (0,0), (0,0), 0), ('RIGHTPADDING', (0,0), (0,0), 0)]))
    return a

step_w = (IW - 3 * 8*mm) / 4
proc_t = Table([[
    Table([[c] for c in step_cells[0]], colWidths=[step_w]), arrow_cell(),
    Table([[c] for c in step_cells[1]], colWidths=[step_w]), arrow_cell(),
    Table([[c] for c in step_cells[2]], colWidths=[step_w]), arrow_cell(),
    Table([[c] for c in step_cells[3]], colWidths=[step_w]),
]], colWidths=[step_w, 8*mm, step_w, 8*mm, step_w, 8*mm, step_w])
proc_t.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (0,-1), LGRAY), ('BACKGROUND', (2,0), (2,-1), LGRAY),
    ('BACKGROUND', (4,0), (4,-1), LGRAY), ('BACKGROUND', (6,0), (6,-1), LGRAY),
    ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('TOPPADDING', (0,0), (-1,-1), 12), ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LINEBEFORE', (0,0), (0,-1), 3, GOLD), ('LINEBEFORE', (2,0), (2,-1), 3, GOLD),
    ('LINEBEFORE', (4,0), (4,-1), 3, GOLD), ('LINEBEFORE', (6,0), (6,-1), 3, GOLD),
]))
story.append(proc_t)
story.append(PageBreak())

# PAGE 8 — TESTIMONIALS
story += section_header('06  CLIENT RESULTS', 'What Our Clients Say',
    'From first-time investors to established multinationals - here is what businesses across Tanzania say about Banshap.')
tms = [
    ('Banshap handled our entire BRELA registration and business licence applications in under a week. What we were told would take a month was done in four business days. Exceptional professionalism from start to finish.', 'Emmanuel Kariuki', 'Chief Executive Officer', 'Kariuki Trading Co.'),
    ('Our logistics costs dropped 22% in the first quarter after engaging Banshap for route planning and freight consolidation. Their team understands the Tanzania corridor like no other firm we have worked with.', 'Amina Msangi', 'Procurement Director', 'Agro Exports Ltd.'),
    ('As a foreign investor entering the Tanzanian market, the regulatory landscape was daunting. Banshap guided us through every step - from company incorporation to sector licences - with transparency and speed.', 'Sarah Odhiambo', 'Country Manager', 'NovaBridge Capital'),
]
for q, name, role, company in tms:
    story.append(testimonial_card(q, name, role, company))
    story.append(Spacer(1, 4*mm))
story.append(Spacer(1, 4*mm))
story.append(Paragraph('MEASURABLE CLIENT OUTCOMES', S['secLabel']))
story.append(Spacer(1, 3*mm))
story.append(make_kpi_row([('22%', 'Avg Logistics Cost Reduction'), ('<4 Days', 'Avg BRELA Registration'), ('100%', 'Regulatory Compliance Rate'), ('500+', 'Businesses Since 2010')], bg=NAVY))
story.append(PageBreak())

# PAGE 9 — LEADERSHIP TEAM
story += section_header('07  OUR PEOPLE', 'Leadership Team',
    'The professionals behind every successful engagement - specialists united by a single purpose.')

team = [
    ('Sharifu Mtuta', 'Chief Executive Officer',
     "Visionary leader and co-founder of Banshap Investment Company Limited. Drives the company's strategic direction, client partnerships, and long-term growth across Tanzania's logistics, compliance, and investment sectors."),
    ('Adam Sharifu', 'Managing Director',
     "Oversees day-to-day operations and corporate governance at Banshap. Brings deep expertise in business facilitation, regulatory navigation, and organisational leadership across Tanzania's commercial landscape."),
    ('Emmanuel Ntiga', 'Operations Manager',
     'Manages end-to-end logistics operations, freight coordination, and service delivery across all active client engagements. Ensures operational reliability and performance standards are consistently met.'),
    ('Glory Kessy', 'Accounts Manager',
     'Responsible for financial management, client billing, and TRA compliance reporting. Ensures all financial records are accurate, current, and fully compliant with Tanzanian regulatory requirements.'),
    ('Khadija', 'Human Resources Manager',
     'Leads talent acquisition, staff development, and organisational culture at Banshap. Committed to building a high-performing team that delivers exceptional service to every client.'),
]
team_cards = [team_card(*m, width=IW/2 - 3*mm) for m in team]
team_rows = [team_cards[i:i+2] for i in range(0, len(team_cards), 2)]
tm_t = Table(team_rows, colWidths=[IW/2 - 3*mm, IW/2 - 3*mm], spaceAfter=5*mm)
tm_t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (0,-1), 5), ('RIGHTPADDING', (-1,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
story.append(tm_t)
story.append(PageBreak())

# PAGE 10 — TRUST & COMPLIANCE
story += section_header('08  TRUST & COMPLIANCE', 'Our Regulatory Standing',
    "Fully registered, compliant, and operationally verified - at every level of Tanzania's regulatory framework.")
regs = [
    ('BRELA', 'Business Registrations & Licensing Agency', 'Fully incorporated under BRELA. Certificate of incorporation issued. Annual returns filed and current.'),
    ('TRA', 'Tanzania Revenue Authority', 'Registered taxpayer with active TIN and VAT status. CPA-T qualified team managing full tax compliance.'),
    ('SUMATRA', 'Surface & Marine Transport Regulatory Authority', 'All vehicle fleet operations comply with SUMATRA licensing requirements. Fleet documentation current.'),
    ('TFDA / TBS', 'Tanzania Food & Drugs Authority & Bureau of Standards', 'Agricultural supply operations compliant with TFDA and TBS standards for agri-input distribution.'),
    ('NEMC', 'National Environment Management Council', 'Environmental compliance maintained for all logistics operations in environmentally sensitive corridors.'),
    ('ISO Aligned', 'Quality Management Standard', 'Operational processes aligned with ISO quality management principles - consistent, auditable, and measurable.'),
]
reg_cards = []
for badge, full, desc in regs:
    num = Table([[Paragraph('<b>%s</b>' % badge, ps('_rn', fontName='Helvetica-Bold', fontSize=9, textColor=WHITE, alignment=TA_CENTER))]], colWidths=[20*mm], rowHeights=[10*mm])
    num.setStyle(TableStyle([('BACKGROUND', (0,0), (0,0), NAVY), ('TOPPADDING', (0,0), (0,0), 3), ('BOTTOMPADDING', (0,0), (0,0), 3), ('LEFTPADDING', (0,0), (0,0), 2), ('RIGHTPADDING', (0,0), (0,0), 2), ('ROUNDEDCORNERS', [3])]))
    reg_cards.append([num, Spacer(1, 3*mm), Paragraph(full, S['trustLbl']), Paragraph(desc, S['trustDesc'])])
reg_rows = [reg_cards[i:i+3] for i in range(0, len(reg_cards), 3)]
rt = Table(reg_rows, colWidths=[IW/3]*3)
rt.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BACKGROUND', (0,0), (-1,-1), LGRAY), ('GRID', (0,0), (-1,-1), 0.3, BORDER), ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('LEFTPADDING', (0,0), (-1,-1), 12), ('RIGHTPADDING', (0,0), (-1,-1), 12), ('TOPPADDING', (0,0), (-1,-1), 12), ('BOTTOMPADDING', (0,0), (-1,-1), 12)]))
story.append(rt)
story.append(Spacer(1, 7*mm))
comp = Table([[Paragraph('COMPLIANCE DECLARATION', S['secLabel']), Paragraph('Banshap Investment Company Limited operates in full compliance with all applicable laws, regulations, and professional standards of the United Republic of Tanzania. All client engagements are conducted with complete transparency, documented accountability, and strict adherence to anti-corruption and anti-money laundering frameworks.', S['bodyW'])]], colWidths=[42*mm, IW - 42*mm])
comp.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), NAVY), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14), ('TOPPADDING', (0,0), (-1,-1), 14), ('BOTTOMPADDING', (0,0), (-1,-1), 14), ('ROUNDEDCORNERS', [5]), ('LINEBEFORE', (1,0), (1,-1), 4, GOLD)]))
story.append(comp)
story.append(Spacer(1, 7*mm))
sectors = ['Banking & Finance', 'Agriculture & Agribusiness', 'Manufacturing', 'NGOs & Development', 'Government & Parastatal', 'Retail & FMCG', 'Healthcare & Pharma', 'Construction & Engineering', 'Transport & Logistics', 'Technology & Telecoms']
sec_cells = [Paragraph('  %s' % s, ps('_sc', fontName='Helvetica', fontSize=8.5, textColor=NAVY)) for s in sectors]
sec_t = Table([sec_cells[:5], sec_cells[5:]], colWidths=[IW/5]*5)
sec_t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), LGRAY), ('GRID', (0,0), (-1,-1), 0.3, BORDER), ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7), ('LEFTPADDING', (0,0), (-1,-1), 8), ('LINEBEFORE', (0,0), (0,-1), 3, GOLD)]))
story.append(sec_t)
story.append(PageBreak())

# PAGE 11 — CONTACT
story += section_header('09  GET IN TOUCH', 'Request a Consultation',
    'We respond to all consultation requests within 24 hours. Our specialists are ready to assess your needs.')
contact_items = [
    ('OFFICE ADDRESS', 'Mkwepu & Samora Street, Samora Avenue\nNear Salamanda Tower\nDar es Salaam, Tanzania'),
    ('TELEPHONE', '+255 716 628 867'),
    ('EMAIL ADDRESSES', 'sharifu.mtuta@banshapinvestment.co.tz\nadam.sharifu@banshapinvestment.co.tz'),
    ('BUSINESS HOURS', 'Monday - Friday:  08:00 - 17:30\nSaturday:  09:00 - 13:00'),
]
contact_cells = [[Paragraph(lbl, S['ctaLabel']), Paragraph(val, S['ctaVal'])] for lbl, val in contact_items]
ct = Table(contact_cells, colWidths=[38*mm, IW - 38*mm])
ct.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), NAVY), ('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 14), ('RIGHTPADDING', (0,0), (-1,-1), 14), ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8), ('LINEBELOW', (0,0), (-1,-4), 0.3, DIVIDER), ('LINEBELOW', (0,1), (-1,-3), 0.3, DIVIDER), ('LINEBELOW', (0,2), (-1,-2), 0.3, DIVIDER), ('ROUNDEDCORNERS', [6]), ('LINEBEFORE', (1,0), (1,-1), 1, DIVIDER)]))
story.append(ct)
story.append(Spacer(1, 6*mm))
story.append(Paragraph('NATIONWIDE PRESENCE', S['secLabel']))
story.append(Spacer(1, 3*mm))
cities = [('Dar es Salaam', 'Headquarters & Main Operations'), ('Dodoma', 'Central Region Hub'), ('Arusha', 'Northern Corridor Office'), ('Mwanza', 'Lake Zone Operations'), ('Mbeya', 'Southern Highlands Office'), ('Zanzibar', 'Island Operations'), ('Morogoro', 'Eastern Zone Agent'), ('Tanga', 'Tanga Port Liaison'), ('Mtwara', 'Southern Zone Agent'), ('Kigoma', 'Western Zone Agent'), ('Tabora', 'Central Zone Agent'), ('Iringa', 'Highlands Agent')]
city_rows = []
for i in range(0, len(cities), 4):
    row = []
    for city, role in cities[i:i+4]:
        row.append([Paragraph('<b>%s</b>' % city, ps('_cy', fontName='Helvetica-Bold', fontSize=8.5, textColor=NAVY, spaceAfter=1)), Paragraph(role, S['caption'])])
    while len(row) < 4:
        row.append([Spacer(1,1)])
    city_rows.append(row)
city_t = Table(city_rows, colWidths=[IW/4]*4)
city_t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), LGRAY), ('GRID', (0,0), (-1,-1), 0.3, BORDER), ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7), ('LEFTPADDING', (0,0), (-1,-1), 10)]))
story.append(city_t)
story.append(Spacer(1, 7*mm))

cta_btn = Table([[Paragraph('REQUEST A CONSULTATION', ps('_b', fontName='Helvetica-Bold', fontSize=10, textColor=NAVY, alignment=TA_CENTER))]], colWidths=[80*mm], rowHeights=[12*mm], hAlign='CENTER')
cta_btn.setStyle(TableStyle([('BACKGROUND', (0,0), (0,0), GOLD), ('TOPPADDING', (0,0), (0,0), 5), ('BOTTOMPADDING', (0,0), (0,0), 5), ('ROUNDEDCORNERS', [5])]))
cta_content = [
    Paragraph('START YOUR JOURNEY WITH BANSHAP', ps('_h', fontName='Helvetica-Bold', fontSize=15, textColor=WHITE, alignment=TA_CENTER, spaceAfter=6)),
    Paragraph('+255 716 628 867  -  sharifu.mtuta@banshapinvestment.co.tz', ps('_c', fontName='Helvetica', fontSize=10, textColor=LBLUE, alignment=TA_CENTER, spaceAfter=6)),
    Paragraph('We respond to all enquiries within 24 hours.', ps('_s', fontName='Helvetica', fontSize=9, textColor=MGRAY, alignment=TA_CENTER, spaceAfter=12)),
    cta_btn,
]
cta_outer = Table([[cta_content]], colWidths=[IW])
cta_outer.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), NAVY), ('LEFTPADDING', (0,0), (-1,-1), 30), ('RIGHTPADDING', (0,0), (-1,-1), 30), ('TOPPADDING', (0,0), (-1,-1), 24), ('BOTTOMPADDING', (0,0), (-1,-1), 24), ('ROUNDEDCORNERS', [8])]))
story.append(cta_outer)

# ── BUILD PDF ─────────────────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(script_dir, 'Banshap_Company_Profile_Premium_2025.pdf')

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=M, rightMargin=M,
    topMargin=17*mm, bottomMargin=14*mm,
    title='Banshap Investment Company Limited - Company Profile 2025',
    author='Banshap Investment Company Limited',
    subject='Corporate Company Profile',
    creator='Banshap',
)
doc.build(story, onFirstPage=page_cb, onLaterPages=page_cb)
print('SUCCESS! PDF saved to:', OUT)
